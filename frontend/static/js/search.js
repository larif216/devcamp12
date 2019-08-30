function getPrediction() {
    $(document).ready(function () {
        var selectedProd = $('#product').val();
        var id = indexProd.findIndex(k=> k == selectedProd);
        geograph(selectedProd);
        // $.ajax({
        //     url: '/api/predict/' + id + '/',
        //     success: function (result) {
        //         console.log(result);
        //     }
        // })
    })
}