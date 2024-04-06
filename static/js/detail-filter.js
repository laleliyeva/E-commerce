const color = document.querySelectorAll('.col-filter')
console.log(color);
color.forEach((element) => {
    element.addEventListener('click', () => {
        let url = `${location.origin}/api/products/${element.getAttribute('data-product')}/versions/${element.getAttribute('data-version')}/`
        url += `?color=${element.getAttribute('data-version')}`
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                document.getElementById('cover_image').innerHTML = `
                    <div id="image1" class="tab-pane fade show active">
                        <div class="simpleLens-big-image-container">
                            <a class="simpleLens-lens-image" data-lens-image="${data['cover_image']}">
                                <img alt="" src="${data['cover_image']}" class="simpleLens-big-image">
                            </a>
                        </div>
                    </div>
                    
                `
                document.getElementById('wishlist').innerHTML = `
                    <li class = 'wishlist' data-id = '${data['id']}'><i  data-id = '${data['id']}' class="fa fa-heart"></i></li>
                `
                document.getElementById('basket').innerHTML = `
                    <button id = 'basket-detail' data-id='${data['id']}' class="button2 btn-cart"  title="" type="button">
                        <span  data-id='${data['id']}'>Add to Cart</span>
                    </button>
                `
                getWishlist()
                getBasketdetail()

            })
    });
});


function getBasketdetail() {
    const basketdetail = document.querySelector('#basket-detail');
    const quantity = document.querySelector("#qty")
    basketdetail.addEventListener('click', (element) => {
        return fetch(`${location.origin}/api/basket/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'product': element.target.dataset.id,
                'quantity': parseInt(quantity.value)
            })

        })
            .then((response) => {
                if (response.status === 201) {
                    alert('Added to Basket!');
                }
            })
    })
}
getBasketdetail()


