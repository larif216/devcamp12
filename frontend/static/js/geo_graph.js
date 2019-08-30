
function geograph(product) {
    var dataInput = [];
    for (i = 0; i < product.region.length; i++) {
        dataInput[i] = {
            y: product.region[i].sum,
            label: product.region[i].name
        }
    }
    $('.card').show();
    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light2", // "light1", "light2", "dark1", "dark2"
        title:{
            text: "Prediksi Jumlah Permintaan "+ product.name +" Berdasarkan Regional"
        },
        data: [{        
            type: "column",  
            showInLegend: true, 
            legendText: "Region",
            dataPoints: dataInput,
            click: function(e){
                var selectedRegion = product.region.findIndex(k => k.name == e.dataPoint.label);
                linegraph(product, selectedRegion);
            }
        }
    ]
    });
    chart.render();
    }