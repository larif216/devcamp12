function getPrediction() {
    $(document).ready(function () {
        var selectedProd = $('#product').val();
        var id = indexProd.findIndex(k=> k == selectedProd);
        if (selectedProd == '') {
            return
        }
        $.ajax({
            url: '/api/predict/' + id + '/',
            success: function (result) {
                geograph(result);
            }
        })
    })
}