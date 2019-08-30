
function geograph(namaProduct) {

    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light2", // "light1", "light2", "dark1", "dark2"
        title:{
            text: "Prediksi Jumlah Permintaan "+namaProduct+" Berdasarkan Regional"
        },
        data: [{        
            type: "column",  
            showInLegend: true, 
            legendText: "Region",
            dataPoints: [      
                { y: 300878, label: "Sumatera Barat" },
                { y: 266455,  label: "Kalimantan Utara" },
                { y: 169709,  label: "Jawa Timur" }
            ],
            click: function(e){
                linegraph(e.label);
            }
        }
    ]
    });
    chart.render();
    }