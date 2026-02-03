function getprodata() {
        var xhttp = new XMLHttpRequest()
        xhttp.open("GET", "/getproduct/" + document.getElementById("Enter product name").value, true)
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var datas = JSON.parse(this.responseText)
                console.log(datas.produ)
                str = '<table>'
                for (x of datas.produ) {
                    str = str + '<tr>'
                    str = str + '<td>' + x.name + '</td>'
                }
                str = str + '</table>'
                document.getElementById("data").innerHTML = str
            }
        };
        xhttp.send();
    }


   