'use strict';
// Presentation only: preloader, hero stats, plant ticker, scroll reveal. No evidence logic lives here.
(() => {
  const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  const $ = (id) => document.getElementById(id);
  const pre = $('preloader');
  if (pre) {
    const count = $('pl-count');
    const done = () => {
      pre.classList.add('done');
      setTimeout(() => pre.remove(), 600);
    };
    if (reduce) done();
    else {
      let n = 0;
      const tick = setInterval(() => {
        n = Math.min(100, n + 7 + Math.floor(Math.random() * 9));
        count.textContent = String(n).padStart(2, '0') + '%';
        pre.style.setProperty('--p', n + '%');
        if (n >= 100) {
          clearInterval(tick);
          setTimeout(done, 180);
        }
      }, 45);
    }
  }
  const data = window.ETHNOTRACE_DATA;
  if (data?.claims) {
    const names = (c) => [].concat(c.claim?.species || []).map(String);
    const species = [...new Set(data.claims.flatMap(names))];
    const extracted = new Set();
    const papers = new Set();
    for (const c of data.claims)
      for (const r of c.results || []) {
        if (r.evidence_level === 'selected_full_text_experimental_unit') extracted.add(r.evidence_id);
        if (r.paper_id) papers.add(r.paper_id);
      }
    const stats = [
      [data.claims.length, 'traditional accounts'],
      [species.length, 'identified species'],
      [extracted.size, 'extracted experiments'],
      [papers.size, 'candidate publications'],
    ];
    const box = $('hero-stats');
    if (box) {
      box.innerHTML = stats
        .map(([n, l]) => `<div><dt>${l}</dt><dd data-n="${n}">${reduce ? n : 0}</dd></div>`)
        .join('');
      if (!reduce)
        box.querySelectorAll('dd').forEach((el) => {
          const end = +el.dataset.n,
            t0 = performance.now() + 700;
          const step = (now) => {
            const k = Math.min(1, Math.max(0, (now - t0) / 1100));
            el.textContent = Math.round(end * (1 - Math.pow(1 - k, 3)));
            if (k < 1) requestAnimationFrame(step);
          };
          requestAnimationFrame(step);
        });
    }
    const track = $('ticker');
    if (track && species.length) {
      const run = species.map((n) => `<span>${n.replace(/[&<>"']/g, '')}</span>`).join('');
      track.innerHTML = run + run;
    }
  }
  const targets = document.querySelectorAll('.atlas, .workspace, .review, #evaluation > *');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(
      (entries) =>
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add('in');
            io.unobserve(e.target);
          }
        }),
      { threshold: 0.08 },
    );
    targets.forEach((el) => {
      el.classList.add('reveal');
      io.observe(el);
    });
  }
})();
