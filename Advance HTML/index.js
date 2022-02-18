//localStorage.clear();
var i=0;
var pname=[];
var unit=[];
var price=[];
var description=[];
var id=[]

function tosubmit() {
    if(localStorage.getItem("pname"))
    {
        pname = eval(localStorage.getItem("pname"));
        unit = eval(localStorage.getItem("unit"));
        price = eval(localStorage.getItem("price"));
        description = eval(localStorage.getItem("description"));
        id=eval(localStorage.getItem("id"));
    }
    i=pname.length;
    pname[i] = document.getElementById("pname").value;
    unit[i] = document.getElementById("unit").value;
    price[i] = document.getElementById("price").value;
    description[i] = document.getElementById("description").value;
    id[i]=i;
    localStorage.setItem("pname", JSON.stringify(pname));
    localStorage.setItem("unit", JSON.stringify(unit));
    localStorage.setItem("price", JSON.stringify(price));
    localStorage.setItem("description", JSON.stringify(description));
    localStorage.setItem("id", JSON.stringify(id));
    }


function init() {

    var pname = eval(localStorage.getItem("pname"));
    var unit = eval(localStorage.getItem("unit"));
    var price = eval(localStorage.getItem("price"));
    var description = eval(localStorage.getItem("description"));
    var id = eval(localStorage.getItem("id"));

    var table=document.getElementById("table");
    for(j=0;j<pname.length;j++)
    {
    var row=table.insertRow();
    row.innerHTML="<td>"+id[j]+"</td>"+"<td>"+pname[j]+"</td>"+"<td>"+description[j]+"</td>"+"<td>"+price[j]+"</td>"+"<td>"+unit[j]+"</td>"+"<td>"+"<button onclick=edit("+id[j]+");>"+"Edit"+"</button>"+"</td>"+"<td>"+"<button onclick=del("+id[j]+");>"+"Delete"+"</button>"+"</td>";
    }
}


function edit(k){
    var pname = eval(localStorage.getItem("pname"));
    var unit = eval(localStorage.getItem("unit"));
    var price = eval(localStorage.getItem("price"));
    var description = eval(localStorage.getItem("description"));
    var id = eval(localStorage.getItem("id"));

    var tpname=pname[k];
    var tunit=unit[k];
    var tprice=price[k];
    var tdescription=description[k];
    var tid=id[k];

    localStorage.setItem("tpname", tpname);
    localStorage.setItem("tunit", tunit);
    localStorage.setItem("tprice", tprice);
    localStorage.setItem("tdescription", tdescription);
    localStorage.setItem("tid", tid);
    del(k);
    window.location.href="index.html";
}

function edit2()
{
    var k=localStorage.getItem("tid");
    if(localStorage.getItem("tpname")!=undefined)
    {
        document.getElementById("pname").value=localStorage.getItem("tpname");
        document.getElementById("unit").value=localStorage.getItem("tunit");
        document.getElementById("price").value=localStorage.getItem("tprice");
        document.getElementById("description").value=localStorage.getItem("tdescription");
        localStorage.removeItem("tpname"); 
        localStorage.removeItem("tunit"); 
        localStorage.removeItem("tprice"); 
        localStorage.removeItem("tdescription"); 
        localStorage.removeItem("tid"); 
    }
       
}

function del(k){
    var pname = eval(localStorage.getItem("pname"));
    var unit = eval(localStorage.getItem("unit"));
    var price = eval(localStorage.getItem("price"));
    var description = eval(localStorage.getItem("description"));
    var id = eval(localStorage.getItem("id"));
    pname.splice(k, 1);
    unit.splice(k, 1);
    price.splice(k, 1);
    description.splice(k, 1);
    id.splice(k, 1);
    localStorage.setItem("pname", JSON.stringify(pname));
    localStorage.setItem("unit", JSON.stringify(unit));
    localStorage.setItem("price", JSON.stringify(price));
    localStorage.setItem("description", JSON.stringify(description));
    localStorage.setItem("id", JSON.stringify(id));
    location.reload();  
}

