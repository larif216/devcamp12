function getPrediction() {
    $(document).ready(function () {
        var selectedProd = $('#product').val();
        var id = indexProd.findIndex(k=> k == selectedProd) + 1;
        if (selectedProd == '') {
            return
        }
        $('html').css('background', 'white');
        $.ajax({
            url: '/api/predict/' + id + '/',
            success: function (result) {
                geograph(result);
            }
        })
    })
}