/* bellakoosh.com — progressive enhancement only.
   Every page is fully readable with JavaScript disabled. */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- Mobile navigation ---- */
  var toggle = document.querySelector(".navtoggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", String(!open));
      toggle.setAttribute("aria-expanded", String(!open));
      toggle.querySelector("[data-label]").textContent = open ? "Menu" : "Close";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
        toggle.querySelector("[data-label]").textContent = "Menu";
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.getAttribute("data-open") === "true") {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
        toggle.querySelector("[data-label]").textContent = "Menu";
        toggle.focus();
      }
    });
  }

  /* ---- Scroll reveal, staggered on a 1/16-note grid at 120 BPM ---- */
  var rises = document.querySelectorAll(".rise");
  if (reduced || !("IntersectionObserver" in window)) {
    rises.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var group = entry.target.parentElement
          ? Array.prototype.indexOf.call(entry.target.parentElement.children, entry.target)
          : 0;
        entry.target.style.setProperty("--d", Math.min(group, 5) * 125 + "ms");
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });
    rises.forEach(function (el) { io.observe(el); });
  }

  /* ---- Reading progress "needle" ---- */
  var needle = document.querySelector(".needle");
  if (needle && !reduced) {
    var tick = false;
    var update = function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? window.scrollY / h : 0;
      needle.style.transform = "scaleX(" + Math.min(1, Math.max(0, p)) + ")";
      tick = false;
    };
    window.addEventListener("scroll", function () {
      if (!tick) { tick = true; window.requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  /* ---- Case-study section nav highlighting ---- */
  var csLinks = document.querySelectorAll(".csnav a[href^='#']");
  if (csLinks.length && "IntersectionObserver" in window) {
    var map = {};
    csLinks.forEach(function (a) {
      var t = document.querySelector(a.getAttribute("href"));
      if (t) map[t.id] = a;
    });
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          csLinks.forEach(function (a) { a.classList.remove("is-active"); });
          if (map[entry.target.id]) map[entry.target.id].classList.add("is-active");
        }
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) so.observe(el);
    });
  }
})();
