var indexProd = [];
var product = [];

$(document).ready(function () {
    $('.card').hide();
    $.ajax({
        url: '/api/product/',
        success: function (pro) {
            var i;
            // product_obj = pro.product;
            for (i = 0; i < pro.product.length; i++) {
                product[i] = pro.product[i];
                indexProd[i] = pro.product[i].value;
            }
            // autocomplete(document.getElementById("product"), product);
        }
    });

    $("form").submit(function (e) {
        e.preventDefault();
    });

    $("#product").autocomplete({
        lookup: product,
        onSelect:function (prod) {
            $('#product').val(prod.value);
        }
    });
});
