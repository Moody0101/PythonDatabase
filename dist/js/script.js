const accnts = document.querySelector(".accounts");
const ps = document.querySelector(".passwords");
let req = new XMLHttpRequest();
req.onreadystatechange = () => {
    if(req.readyState == 4 && req.status == 200) {
        res = req.responseText;
        data = JSON.parse(res);
        if(data.accounts.length > 0) {
            for(i in data.accounts) {
                const e = document.createElement("span");
                e.textContent = String(data.accounts[i]);
                accnts.appendChild(e);
            }
            for(i in data.passwords) {
                const e = document.createElement("span");
                e.textContent = String(data.passwords[i]);
                ps.appendChild(e);
            }
        }
    }
}

req.open("GET", "../db.json", true);
req.send();