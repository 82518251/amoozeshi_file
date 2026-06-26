
function addProductToOrder(productId) {
    const productCount = $('#product_count').val();
    $.get('/order/add-to-order?product_id='+productId+'&count=' +productCount).then(res=>{

        swal.fire({
            title : "",
            text: res.text,
            icon: res.icon,
            showCancelButton : false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirmButtonText
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_user') {
            window.location.href= '/account/login'
            }
        });
    });
}

function removeOrderDetail(detailId) {
    $.get('/dashboard/remove-order-detail?detail_id=' +detailId).then(res=> {
        if (res.status == 'success') {
            $('#order-detail-count').html(res.body);
        }
    });
}
function changeOrderDetailCount(detailId, state) {
    $.get('/dashboard/change-order-detail?detail_id=' +detailId+'&state='+state).then(res=> {
        if (res.status === 'success') {
            $('#order-detail-count').html(res.body);
        }
    });
}