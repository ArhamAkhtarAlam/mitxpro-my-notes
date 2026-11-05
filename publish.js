// drag the right edge of the sidebar to resize it, double click to reset
(function () {
  const KEY = "sidebar-width", MIN = 180, MAX = 600;

  function setup() {
    const side = document.querySelector(".site-body-left-column");
    if (!side || side.querySelector(".sidebar-resizer")) return !!side;

    if (getComputedStyle(side).position === "static") side.style.position = "relative";

    const apply = (w) => {
      w = Math.min(MAX, Math.max(MIN, w));
      side.style.width = side.style.minWidth = side.style.maxWidth = w + "px";
      side.style.flex = `0 0 ${w}px`;
      document.documentElement.style.setProperty("--sidebar-width", w + "px");
      return w;
    };

    let saved = NaN;
    try { saved = parseInt(localStorage.getItem(KEY), 10); } catch (e) {}
    if (saved) apply(saved);

    const handle = document.createElement("div");
    handle.className = "sidebar-resizer";
    side.appendChild(handle);

    handle.addEventListener("pointerdown", (e) => {
      e.preventDefault();
      handle.setPointerCapture(e.pointerId);
      document.body.classList.add("sidebar-resizing");
      const left = side.getBoundingClientRect().left;
      const move = (ev) => apply(ev.clientX - left);
      const up = () => {
        try { localStorage.setItem(KEY, parseInt(side.style.width, 10)); } catch (e) {}
        document.body.classList.remove("sidebar-resizing");
        handle.removeEventListener("pointermove", move);
        handle.removeEventListener("pointerup", up);
      };
      handle.addEventListener("pointermove", move);
      handle.addEventListener("pointerup", up);
    });

    handle.addEventListener("dblclick", () => {
      try { localStorage.removeItem(KEY); } catch (e) {}
      ["width", "minWidth", "maxWidth", "flex"].forEach((p) => (side.style[p] = ""));
    });
    return true;
  }

  // Publish is a single-page app, so wait for the sidebar to exist
  const t = setInterval(() => { if (setup()) clearInterval(t); }, 300);
})();
