(function(){
  var c=document.getElementById("calc"); if(!c) return;
  var loc=c.dataset.locale, cost=c.querySelector("#cost"), shifts=c.querySelector("#shifts");
  var fmt=function(n){return n.toLocaleString(loc,{style:"currency",currency:"EUR",maximumFractionDigits:0});};
  function upd(){
    var v=Math.max(0,parseFloat(cost.value)||0);
    var n=parseInt(shifts.value,10)||1, now=v*n, you=now*0.7, save=now-you;
    c.querySelector("#o-now").textContent=fmt(now);
    c.querySelector("#o-you").textContent=fmt(you);
    c.querySelector("#o-m").textContent=fmt(save);
    c.querySelector("#o-y").textContent=fmt(save*12);
  }
  cost.addEventListener("input",upd); shifts.addEventListener("change",upd); upd();
})();
