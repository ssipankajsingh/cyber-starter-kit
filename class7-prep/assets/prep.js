/* Class 7 prep: interactive practice, progress and streaks.
   Everything is stored in this browser only (localStorage). Nothing is sent anywhere. */
(function () {
  "use strict";

  var NS = "c7.";
  var TOTAL_TOPICS = 26;

  function load(key, fallback) {
    try {
      var v = window.localStorage.getItem(NS + key);
      return v ? JSON.parse(v) : fallback;
    } catch (e) { return fallback; }
  }
  function save(key, value) {
    try { window.localStorage.setItem(NS + key, JSON.stringify(value)); } catch (e) { /* storage blocked */ }
  }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function dayString(d) { return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); }

  var C7 = {};
  window.C7 = C7;

  /* "mathematics/3-algebraic-expressions" from any page address under class7-prep */
  C7.pageKey = function (path) {
    var p;
    try { p = decodeURIComponent(path || window.location.pathname); } catch (e) { p = path || window.location.pathname; }
    var i = p.indexOf("class7-prep/");
    if (i < 0) { return null; }
    p = p.slice(i + "class7-prep/".length).replace(/\.html$/, "").replace(/\/$/, "");
    return p || "index";
  };

  /* ---------- streak ---------- */
  C7.markActive = function () {
    var days = load("days", []);
    var t = dayString(new Date());
    if (days.indexOf(t) < 0) {
      days.push(t);
      if (days.length > 400) { days = days.slice(days.length - 400); }
      save("days", days);
    }
  };
  C7.streak = function () {
    var days = load("days", []);
    var d = new Date();
    if (days.indexOf(dayString(d)) < 0) { d.setDate(d.getDate() - 1); }
    var n = 0;
    while (days.indexOf(dayString(d)) >= 0) { n += 1; d.setDate(d.getDate() - 1); }
    return n;
  };

  /* ---------- practice progress ---------- */
  C7.savePractice = function (key, total, results) {
    var all = load("practice", {});
    all[key] = { t: total, r: results };
    save("practice", all);
  };
  C7.topicProgress = function (key) {
    var p = load("practice", {})[key];
    if (!p) { return { total: 0, ok: 0, checked: 0 }; }
    var ok = 0, checked = 0, k;
    for (k in p.r) {
      if (Object.prototype.hasOwnProperty.call(p.r, k)) {
        checked += 1;
        if (p.r[k] === "ok") { ok += 1; }
      }
    }
    return { total: p.t, ok: ok, checked: checked };
  };

  /* ---------- quiz scores ---------- */
  C7.getQuiz = function (subject, chapter) {
    var q = load("quiz", {});
    return q[subject] && q[subject][chapter] ? q[subject][chapter] : null;
  };
  C7.saveQuiz = function (subject, chapter, right, total) {
    var all = load("quiz", {});
    all[subject] = all[subject] || {};
    var prev = all[subject][chapter] || null;
    var better = !prev || right / total > prev.best / prev.total;
    if (better) { all[subject][chapter] = { best: right, total: total }; }
    save("quiz", all);
    C7.markActive();
    return { prev: prev, best: better ? { best: right, total: total } : prev };
  };

  /* ---------- stars for a topic (0 to 3) ---------- */
  C7.topicStars = function (key) {
    var p = C7.topicProgress(key);
    if (!p.total) { return 0; }
    var pct = p.ok / p.total;
    var stars = 0;
    if (pct >= 0.5) { stars = 1; }
    if (pct >= 0.8) { stars = 2; }
    if (stars === 2) {
      var m = /^([a-z-]+)\/(\d+)-/.exec(key);
      if (m) {
        var q = C7.getQuiz(m[1], String(parseInt(m[2], 10) - 1));
        if (q && q.best / q.total >= 0.8) { stars = 3; }
      }
    }
    return stars;
  };
  function starText(n) {
    var s = "", i;
    for (i = 0; i < 3; i += 1) { s += i < n ? "★" : "☆"; }
    return s;
  }

  /* ---------- flashcard progress (used by flashcards.html) ---------- */
  C7.getCards = function (deck) { return load("cards." + deck, {}); };
  C7.saveCards = function (deck, boxes) { save("cards." + deck, boxes); };

  /* ---------- styles for the pages that use the script ---------- */
  function injectCSS() {
    if (document.getElementById("c7-css")) { return; }
    var css = [
      ".practice{margin:1rem 0}",
      ".pgroup{font-weight:700;margin:18px 0 4px}",
      ".pnote{margin:6px 0}",
      ".pq{border:1px solid #d5dde5;border-left:6px solid #cbd5e1;border-radius:10px;padding:10px 14px;margin:10px 0;background:#fff}",
      ".pq.ok{border-left-color:#159957;background:#f0fbf4}",
      ".pq.no{border-left-color:#e08a00;background:#fff8ec}",
      ".pqn{font-weight:700;margin-right:4px}",
      ".pqa{margin-top:8px;padding:8px 10px;background:#eaf6f6;border-radius:8px}",
      ".c7-hidden{display:none}",
      ".c7-btns{margin-top:8px;display:flex;flex-wrap:wrap;gap:8px}",
      ".c7-btn{font:inherit;font-size:.95rem;padding:6px 14px;border-radius:8px;border:1px solid #159957;background:#fff;color:#0f6b3d;cursor:pointer}",
      ".c7-btn.primary{background:#159957;color:#fff}",
      ".c7-btn.warn{border-color:#c47a00;color:#8a5200}",
      ".c7-btn:focus-visible{outline:3px solid #1e6bb8;outline-offset:2px}",
      ".c7-tag{margin-left:10px;font-size:.85rem;font-weight:700}",
      ".pq.ok .c7-tag{color:#0f6b3d}",
      ".pq.no .c7-tag{color:#8a5200}",
      ".c7-bar,.c7-panel{background:#f1f6f9;border:1px solid #d5dde5;border-radius:10px;padding:10px 14px;margin:0 0 12px}",
      ".c7-meter{height:8px;background:#d5dde5;border-radius:99px;overflow:hidden;margin:6px 0}",
      ".c7-meter i{display:block;height:100%;background:#159957;width:0;transition:width .3s}",
      ".c7-stars{color:#d99a00;letter-spacing:2px}",
      ".c7-badge{margin-left:8px;font-size:.85rem;color:#4a5560;white-space:nowrap}",
      ".c7-panel b{color:#1f2933}",
      ".c7-cheer{margin-top:6px;font-weight:700;color:#0f6b3d}"
    ].join("\n");
    var el = document.createElement("style");
    el.id = "c7-css";
    el.textContent = css;
    document.head.appendChild(el);
  }

  function button(label, kind, onClick) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "c7-btn" + (kind ? " " + kind : "");
    b.textContent = label;
    b.addEventListener("click", onClick);
    return b;
  }

  /* ---------- tap-to-check practice ---------- */
  function enhancePractice() {
    var box = document.querySelector(".practice");
    if (!box) { return; }
    var key = C7.pageKey();
    if (!key) { return; }
    injectCSS();

    var qs = box.querySelectorAll(".pq");
    var saved = load("practice", {})[key];
    var results = saved && saved.r ? saved.r : {};

    var bar = document.createElement("div");
    bar.className = "c7-bar";
    var line = document.createElement("div");
    var meter = document.createElement("div");
    meter.className = "c7-meter";
    var fill = document.createElement("i");
    meter.appendChild(fill);
    var cheer = document.createElement("div");
    cheer.className = "c7-cheer";
    var resetRow = document.createElement("div");
    resetRow.className = "c7-btns";
    bar.appendChild(line);
    bar.appendChild(meter);
    bar.appendChild(cheer);
    bar.appendChild(resetRow);
    box.insertBefore(bar, box.firstChild);

    function updateBar() {
      var p = { total: qs.length, ok: 0, checked: 0 }, k;
      for (k in results) {
        if (Object.prototype.hasOwnProperty.call(results, k)) {
          p.checked += 1;
          if (results[k] === "ok") { p.ok += 1; }
        }
      }
      C7.savePractice(key, qs.length, results);
      var stars = C7.topicStars(key);
      line.innerHTML = "";
      line.appendChild(document.createTextNode(p.checked + " of " + p.total + " checked, " + p.ok + " got it   "));
      var st = document.createElement("span");
      st.className = "c7-stars";
      st.textContent = starText(stars);
      st.title = "Stars: 1 for 50% got it, 2 for 80%, 3 for 80% plus a quiz score of 80% or more on this topic";
      line.appendChild(st);
      fill.style.width = Math.round(p.checked / p.total * 100) + "%";
      if (p.checked === p.total) {
        cheer.textContent = p.ok / p.total >= 0.8
          ? "All done. Strong work! Try the quiz tomorrow to earn the third star."
          : "All checked. Redo the \"Revise this\" ones tomorrow, then try again.";
      } else {
        cheer.textContent = "";
      }
    }

    resetRow.appendChild(button("Reset this page", "", function () {
      results = {};
      qs.forEach(function (q) { q._c7reset(); });
      updateBar();
    }));

    Array.prototype.forEach.call(qs, function (q, idx) {
      var n = String(idx + 1);
      var ans = q.querySelector(".pqa");
      var head = q.querySelector(".pqt");
      var ctrl = document.createElement("div");
      ctrl.className = "c7-btns";
      q.appendChild(ctrl);
      var phase = "ask";

      function render() {
        var st = results[n];
        q.className = "pq" + (st ? " " + st : "");
        var old = head.querySelector(".c7-tag");
        if (old) { head.removeChild(old); }
        if (st) {
          var tag = document.createElement("span");
          tag.className = "c7-tag";
          tag.textContent = st === "ok" ? "✓ Got it" : "✗ Revise this";
          head.appendChild(tag);
        }
        ctrl.textContent = "";
        if (phase === "shown") {
          ans.classList.remove("c7-hidden");
          ctrl.appendChild(button("I got it", "primary", function () { phase = "ask"; set("ok"); }));
          ctrl.appendChild(button("Not yet", "warn", function () { phase = "ask"; set("no"); }));
        } else {
          ans.classList.add("c7-hidden");
          ctrl.appendChild(button(st ? "See answer again" : "Show answer", st ? "" : "primary", function () { phase = "shown"; render(); }));
          if (st) { ctrl.appendChild(button("Try again", "", function () { set(null); })); }
        }
      }
      function set(st) {
        if (st) { results[n] = st; C7.markActive(); } else { delete results[n]; }
        render();
        updateBar();
      }
      q._c7reset = function () { phase = "ask"; render(); };
      render();
    });
    updateBar();
  }

  /* ---------- badges on index pages ---------- */
  function addBadges() {
    if (document.querySelector(".practice")) { return; }
    var links = document.querySelectorAll("main td a[href], main li a[href], .main-content td a[href], .main-content li a[href]");
    Array.prototype.forEach.call(links, function (a) {
      if (a.getAttribute("data-c7")) { return; }
      var key = C7.pageKey(a.pathname);
      if (!key || !/^[a-z-]+\/\d+-/.test(key)) { return; }
      var p = C7.topicProgress(key);
      if (!p.total || !p.checked) { return; }
      a.setAttribute("data-c7", "1");
      var span = document.createElement("span");
      span.className = "c7-badge";
      var stars = document.createElement("span");
      stars.className = "c7-stars";
      stars.textContent = starText(C7.topicStars(key));
      span.appendChild(stars);
      span.appendChild(document.createTextNode(" " + p.ok + "/" + p.total));
      a.parentNode.insertBefore(span, a.nextSibling);
    });
  }

  /* ---------- progress panel on the prep home page ---------- */
  function renderPanel() {
    var host = document.getElementById("c7-progress");
    if (!host) { return; }
    injectCSS();
    var all = load("practice", {});
    var done = 0, started = 0, k;
    for (k in all) {
      if (Object.prototype.hasOwnProperty.call(all, k) && /^[a-z-]+\/\d+-/.test(k)) {
        var p = C7.topicProgress(k);
        if (p.checked) { started += 1; }
        if (p.total && p.ok / p.total >= 0.8) { done += 1; }
      }
    }
    var quizzes = 0, s, c, qa = load("quiz", {});
    for (s in qa) {
      if (Object.prototype.hasOwnProperty.call(qa, s)) {
        for (c in qa[s]) { if (Object.prototype.hasOwnProperty.call(qa[s], c)) { quizzes += 1; } }
      }
    }
    var streak = C7.streak();
    host.className = "c7-panel";
    host.innerHTML = "";
    var title = document.createElement("div");
    title.innerHTML = "<b>My progress</b> (kept on this device only, never sent anywhere)";
    var body = document.createElement("div");
    body.textContent = "Study streak: " + streak + (streak === 1 ? " day" : " days") +
      "   |   Topics done: " + done + " of " + TOTAL_TOPICS +
      "   |   Topics started: " + started +
      "   |   Quizzes tried: " + quizzes;
    var meter = document.createElement("div");
    meter.className = "c7-meter";
    var fill = document.createElement("i");
    fill.style.width = Math.round(done / TOTAL_TOPICS * 100) + "%";
    meter.appendChild(fill);
    var hint = document.createElement("div");
    hint.textContent = streak === 0
      ? "Do one practice question today to start your streak."
      : "Come back tomorrow to keep your streak going.";
    var row = document.createElement("div");
    row.className = "c7-btns";
    row.appendChild(button("Reset my progress", "warn", function () {
      if (!window.confirm("Clear all your saved progress on this device?")) { return; }
      try {
        var i, drop = [];
        for (i = 0; i < window.localStorage.length; i += 1) {
          var name = window.localStorage.key(i);
          if (name && name.indexOf(NS) === 0) { drop.push(name); }
        }
        drop.forEach(function (n) { window.localStorage.removeItem(n); });
      } catch (e) { /* ignore */ }
      renderPanel();
    }));
    host.appendChild(title);
    host.appendChild(body);
    host.appendChild(meter);
    host.appendChild(hint);
    host.appendChild(row);
  }

  function init() {
    enhancePractice();
    addBadges();
    renderPanel();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
