 function drawalldata() {
        var xhttp = new XMLHttpRequest()
        xhttp.open("GET", "/jdata/", true)
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var datax = JSON.parse(this.responseText)
                console.log(datax.new)
                drawdata(datax)
            }
        };
        xhttp.send();
    }

    function drawdata(datax) {
        const ctx = document.getElementById('myChart');

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: getlabels(datax),
                datasets: [{
                    label: '# of Votes',
                    data: getvalues(datax),
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

    }

    function getlabels(datax) {
        let labels = []
        for (x of datax.new) {
            labels.push(x.name)
        }
        return labels
    }
     function getvalues(datax) {
        let values = []
        for (x of datax.new) {
            values.push(x.price)
        }
        return values
    }