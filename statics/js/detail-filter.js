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
                document.getElementById('title').innerHTML = `
                <div class="tab-content jump">
                 <div id="${data['cover_image']}" class="tab-pane fade show active"></div>
                    <ul  class="tab-menu nav" >
                            ${data.image.map(element => `
                                <li class=""><a data-bs-toggle="tab" href="${element.image}"><img style="height:100px;" alt="" src="${element.image}"></a>
                            `).join('')}       
                    </ul>` 
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
    basketdetail.addEventListener('click' , (element) =>{
        return fetch(`${location.origin}/api/basket/` , {
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


