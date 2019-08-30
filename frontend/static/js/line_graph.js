
function linegraph(product, idRegion){
    var region = product.region[idRegion];
    var starttgl = 20;
    var startbln =12;
    var startthn = 2019;
    var dataInputMerk = [10,2,5,43,5,2,53,2,14,65,7,2,3,15,6,78,23,34,6,4,2,3,41,89,32,56,78,12,34,67];
    var dataInputKategori = [15,8,4,1,35,73,5,4,53,15,6,12,7,2,1,43,89,42,23,98,65,34,67,85,35,63,67,54,76,45];
    var tglskrg = starttgl;
    var blnskrg = startbln-1;
    var thnskrg = startthn;
    var dataMerk = [];
    var dataKategori =[]; 

    for(var i = 0; i < dataInputMerk.length; i++) {
        if(blnskrg==0||blnskrg==2||blnskrg==4||blnskrg==6||blnskrg==7||blnskrg==9||blnskrg==11){
            if(tglskrg == 32){
                if(blnskrg==11){
                    blnskrg = 0;
                    tglskrg = 1;
                    thnskrg = thnskrg+1;
                    dataMerk.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputMerk[i]});
                    dataKategori.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputKategori[i]});
                }
                else{
                    blnskrg = blnskrg+1;
                    tglskrg = 1;
                    dataMerk.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputMerk[i]});
                    dataKategori.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputKategori[i]});
                }
            }
            else{
                dataMerk.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputMerk[i]});
                dataKategori.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputKategori[i]});
                tglskrg = tglskrg+1;
            }
        }
        if(blnskrg==1){
            if(tglskrg == 29){
                blnskrg = blnskrg+1;
                tglskrg = 1;
                dataMerk.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputMerk[i]});
                dataKategori.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputKategori[i]});
            }
            else{
                dataMerk.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputMerk[i]});
                dataKategori.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputKategori[i]});
                tglskrg = tglskrg+1;
            }
        }
        if(blnskrg==3||blnskrg==5||blnskrg==8||blnskrg==10){
            if(tglskrg == 31){
                blnskrg = blnskrg+1;
                tglskrg = 1;
                dataMerk.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputMerk[i]});
                dataKategori.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputKategori[i]});            
            }
            else{
                dataMerk.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputMerk[i]});
                dataKategori.push({x: new Date(thnskrg,blnskrg,tglskrg), y: dataInputKategori[i]});
                tglskrg = tglskrg+1;
            }
        }   
    }
    var chart = new CanvasJS.Chart("chartContainer", {
        title: {
            text: "Prediksi Penjualan " + product.name + " di daerah " + region.name
        },
        axisX: {
            valueFormatString: "DD/MM/YYYY",
            title: "Tanggal dan bulan"
        },
        axisY2: {
            title: "Jumlah perminataan"
        },
        toolTip: {
            shared: true
        },
        legend: {
            cursor: "pointer",
            verticalAlign: "top",
            horizontalAlign: "center",
            dockInsidePlotArea: true,
            itemclick: toogleDataSeries
        },
        data: [{
            type:"line",
            axisYType: "secondary",
            name: "Berdasarkan Merk",
            showInLegend: true,
            markerSize: 0,
            dataPoints: dataMerk
        },
        {
            type: "line",
            axisYType: "secondary",
            name: "Berdasarkan Kategori",
            showInLegend: true,
            markerSize: 0,
            yValueFormatString: "#,###",
            dataPoints: dataKategori
        }]
    });

    chart.render();

    function toogleDataSeries(e){
        if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
            e.dataSeries.visible = false;
        } else{
            e.dataSeries.visible = true;
        }
        chart.render();
    }
}



