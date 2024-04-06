const categories = document.querySelectorAll('.category-filter');


categories.forEach((element) => {
    element.addEventListener('click', () => {
        const category = element.getAttribute('id');

        updateURLAndFetchProducts(category);
    });
});

function updateURLAndFetchProducts(category) {
    let url = `${location.origin}/api/products/`;
    if (category) {
        url += `?category=${category}`;
    }

    fetchProducts(url);
}

function fetchProducts(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            document.getElementById('shop-product').innerHTML = '';
            for (let i in data) {
                document.getElementById('shop-product').innerHTML += `
                    <div class="col-xl-3 col-lg-4 col-md-4">
                    <div class="single-product">
                        <div class="product-img">
                            <a href="${data[i]['detail_url']}">
                                <img class="primary-image" src="${data[i]['product_version'][0]['cover_image']}" alt="" />
                            </a>
                        </div>
                        <div class="product-content">
                            <div class="price-box">
                                <p> ${(data[i]['in_sale'] ? `<span class="old-price">$${data[i]['old_price']}</span><span class="special-price">$${data[i]['price']}</span>` : `$${data[i]['price']}`)} </p>
                            </div>
                            <h2 class="product-name"><a href="${data[i]['detail_url']}">${data[i]['name']}</a></h2>
                            </div>
                            <div class="product-icon">
                                <ul class='d-flex'>
                                    <li class='basket' data-id = '${data[i]['id']}'><i class="fa fa-shopping-cart" data-id = '${data[i]['id']}'></i></li>
                                    <li class = 'wishlist' data-id = '${data[i]['id']}'><i  data-id = '${data[i]['id']}' class="fa fa-heart"></i></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>                
                `;
            }
            getWishlist()
            getBasket()
        })
        .catch(error => console.error("Error fetching data:", error));
}


// MANUFACTURER FILTER

const manufacturer = document.querySelectorAll('.manu-filter');

manufacturer.forEach((element) => {
    element.addEventListener('click', () => {
        const manufac = element.getAttribute('data-id');

        updateURLAndFetchProducts(manufac);
    });
});

function updateURLAndFetchProducts(manufac) {
    let url = `${location.origin}/api/products/`;
    if (manufac) {
        url += `?manufacturer=${manufac}`;
    }

    fetchProducts(url);
}

function fetchProducts(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            document.getElementById('shop-product').innerHTML = '';
            for (let i in data) {
                document.getElementById('shop-product').innerHTML += `
                <div class="col-xl-3 col-lg-4 col-md-4">
                <div class="single-product">
                    <div class="product-img">
                        <a href="${data[i]['detail_url']}">
                            <img class="primary-image" src="${data[i]['product_version'][0]['cover_image']}" alt="" />
                        </a>
                    </div>
                    <div class="product-content">
                        <div class="price-box">
                            <p> ${(data[i]['in_sale'] ? `<span class="old-price">$${data[i]['old_price']}</span><span class="special-price">$${data[i]['price']}</span>` : `$${data[i]['price']}`)} </p>
                        </div>
                        <h2 class="product-name"><a href="${data[i]['detail_url']}">${data[i]['name']}</a></h2>
                        </div>
                        <div class="product-icon">
                            <ul class='d-flex'>
                                <li class='basket' data-id = '${data[i]['id']}'><i class="fa fa-shopping-cart" data-id = '${data[i]['id']}'></i></li>
                                <li class = 'wishlist' data-id = '${data[i]['id']}'><i  data-id = '${data[i]['id']}' class="fa fa-heart"></i></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>                
            `;
            }
            getWishlist()
            getBasket()
        })
        .catch(error => console.error("Error fetching data:", error));
}



const color = document.querySelectorAll('.color-filter')

color.forEach((element) => {
    element.addEventListener('click', () => {
        let url = `${location.origin}/api/product_color/`
        url += `?color=${element.getAttribute('data-id')}`

        fetch(url).then(response => response.json()).then(data => {
            document.getElementById('shop-product').innerHTML = '';
            for (let i in data) {
                document.getElementById('shop-product').innerHTML += `
                <div class="col-xl-3 col-lg-4 col-md-4">
                <div class="single-product">
                    <div class="product-img">
                        <a href="${data[i]['detail_url']}">
                            <img class="primary-image" src="${data[i]['product_version'][0]['cover_image']}" alt="" />
                        </a>
                    </div>
                    <div class="product-content">
                        <div class="price-box">
                            <p> ${(data[i]['in_sale'] ? `<span class="old-price">$${data[i]['old_price']}</span><span class="special-price">$${data[i]['price']}</span>` : `$${data[i]['price']}`)} </p>
                        </div>
                        <h2 class="product-name"><a href="${data[i]['detail_url']}">${data[i]['name']}</a></h2>
                        </div>
                        <div class="product-icon">
                            <ul class='d-flex'>
                                <li class='basket' data-id = '${data[i]['id']}'><i class="fa fa-shopping-cart" data-id = '${data[i]['id']}'></i></li>
                                <li class = 'wishlist' data-id = '${data[i]['id']}'><i  data-id = '${data[i]['id']}' class="fa fa-heart"></i></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>                
            `;
            }
            getWishlist()
            getBasket()
        })
    })
})
