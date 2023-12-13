function init(elemid) {
  let canvas = document.getElementById(elemid),
      ctx = canvas.getContext('2d'),
      w = (canvas.width = window.innerWidth),
      h = (canvas.height = window.innerHeight);

  ctx.fillStyle = 'rgba(30, 30, 30, 1)';
  ctx.fillRect(0, 0, w, h);

  return { ctx: ctx, canvas: canvas };
}
