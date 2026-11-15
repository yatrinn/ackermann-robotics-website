(function(){
  var KEY = "";
  var f = document.getElementById("demo");
  if(!f) return;
  var st = document.getElementById("status");
  var m = f.dataset;
  f.addEventListener("submit", function(e){
    e.preventDefault();
    if(!KEY){ st.textContent = m.err; return; }
    var d = new FormData(f);
    d.append("access_key", KEY);
    d.append("subject", "Demo request from " + (d.get("company") || d.get("name")) + " (ackermann-robotics.org)");
    d.append("from_name", "ackermann-robotics.org");
    var b = f.querySelector("button"); b.disabled = true; st.textContent = m.sending;
    fetch("https://api.web3forms.com/submit", {method:"POST", body:d, headers:{Accept:"application/json"}})
      .then(function(r){ return r.json(); })
      .then(function(j){ if(j.success){ f.reset(); st.textContent = m.ok; } else { st.textContent = m.err; } })
      .catch(function(){ st.textContent = m.err; })
      .finally(function(){ b.disabled = false; });
  });
})();
