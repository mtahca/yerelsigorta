(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var mqMobile = window.matchMedia('(max-width: 991px)');

  /* mobile menu */
  var burger = $('.burger'), nav = $('#nav'), overlay = $('.hdr__overlay');
  function setMenu(o) {
    if (!nav) return;
    nav.classList.toggle('open', o);
    document.body.classList.toggle('menu-open', o);
    if (burger) { burger.setAttribute('aria-expanded', o); burger.setAttribute('aria-label', o ? 'Menüyü kapat' : 'Menüyü aç'); }
  }
  if (burger && nav) {
    burger.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    var cl = $('.nav__close'); if (cl) cl.addEventListener('click', function () { setMenu(false); });
    if (overlay) overlay.addEventListener('click', function () { setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setMenu(false); $$('.nav__item.open').forEach(function (i) { i.classList.remove('open'); }); } });
    window.addEventListener('resize', function () { if (!mqMobile.matches) setMenu(false); });
    $$('#nav a').forEach(function (a) {
      a.addEventListener('click', function (e) {
        if (a.classList.contains('sub-toggle-link')) return;
        setMenu(false);
      });
    });
  }
  /* dropdowns: toggle button (mobile + keyboard), "#" parents */
  function closeOthers(except) { $$('.nav__item.open').forEach(function (i) { if (i !== except) { i.classList.remove('open'); var b = $('.sub-toggle', i); if (b) b.setAttribute('aria-expanded', 'false'); } }); }
  $$('.nav__item.has-sub').forEach(function (li) {
    var btn = $('.sub-toggle', li), link = $('.sub-toggle-link', li);
    function toggle(e) {
      e.preventDefault(); e.stopPropagation();
      var o = !li.classList.contains('open'); closeOthers(li);
      li.classList.toggle('open', o); if (btn) btn.setAttribute('aria-expanded', o);
    }
    if (btn) btn.addEventListener('click', toggle);
    if (link) link.addEventListener('click', function (e) { if (mqMobile.matches || 'ontouchstart' in window) toggle(e); else e.preventDefault(); });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.nav__item')) closeOthers(null); });

  /* about tabs */
  $$('[data-tabs]').forEach(function (w) {
    var tabs = $$('.tab', w), panels = $$('.tabpanel', w);
    function show(i, focus) {
      tabs.forEach(function (t, k) { t.classList.toggle('is-on', k === i); t.setAttribute('aria-selected', k === i); t.tabIndex = k === i ? 0 : -1; });
      panels.forEach(function (p, k) { p.classList.toggle('is-on', k === i); });
      if (focus) tabs[i].focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { show(i); });
      t.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { e.preventDefault(); show((i + 1) % tabs.length, true); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); show((i + tabs.length - 1) % tabs.length, true); }
      });
    });
    show(0);
  });

  /* brand carousel */
  $$('[data-carousel]').forEach(function (c) {
    var tr = $('.carousel__track', c), prev = $('.carousel__btn--prev', c), next = $('.carousel__btn--next', c);
    function step() { var li = tr.children[0]; return li ? li.getBoundingClientRect().width : 200; }
    prev.addEventListener('click', function () { tr.scrollBy({ left: -step(), behavior: 'smooth' }); });
    next.addEventListener('click', function () { tr.scrollBy({ left: step(), behavior: 'smooth' }); });
    var timer = null;
    function auto() {
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      timer = setInterval(function () {
        if (tr.scrollLeft + tr.clientWidth >= tr.scrollWidth - 4) tr.scrollTo({ left: 0, behavior: 'smooth' });
        else tr.scrollBy({ left: step(), behavior: 'smooth' });
      }, 3500);
    }
    c.addEventListener('mouseenter', function () { clearInterval(timer); });
    c.addEventListener('mouseleave', auto);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { clearInterval(timer); if (en[0].isIntersecting) auto(); }).observe(c);
  });

  /* compose forms: build a WhatsApp / mail message (nothing is sent to a server) */
  $$('.compose').forEach(function (f) {
    var err = $('.compose__err', f);
    function build() {
      var topic = f.getAttribute('data-topic'), lines = ['Merhaba, ' + topic + ' ile ilgili bilgi almak istiyorum.', ''];
      var ok = true;
      $$('input,textarea', f).forEach(function (el) {
        var label = el.parentNode.querySelector('span').textContent.replace(/\s*\*$/, '');
        var v = (el.value || '').trim();
        if (el.required && !v) { ok = false; el.classList.add('bad'); } else el.classList.remove('bad');
        if (v) lines.push(label + ': ' + v);
      });
      return ok ? lines.join('\n') : null;
    }
    $$('[data-send]', f).forEach(function (b) {
      b.addEventListener('click', function () {
        var msg = build();
        if (err) err.hidden = !!msg;
        if (!msg) { var bad = $('.bad', f); if (bad) bad.focus(); return; }
        if (b.getAttribute('data-send') === 'wa') {
          window.open('https://wa.me/' + f.getAttribute('data-wa') + '?text=' + encodeURIComponent(msg), '_blank', 'noopener');
        } else {
          location.href = 'mailto:' + f.getAttribute('data-mail') + '?subject=' + encodeURIComponent(f.getAttribute('data-topic') + ' - Talep') + '&body=' + encodeURIComponent(msg);
        }
      });
    });
    f.addEventListener('submit', function (e) { e.preventDefault(); });
  });

  /* back to top */
  var top = $('.toplink');
  if (top) {
    var onScroll = function () { top.hidden = window.scrollY < 300; };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
    top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
  }
})();
