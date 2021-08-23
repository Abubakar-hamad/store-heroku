 <div class="single-product-area">
        <div class="zigzag-bottom"></div>
        <div class="container">
            <div class="row">
                
           
            {% for product in all_product  %}
            <div class="card">
            
            <div class="col-md-4">
                
            
                        <div class="product-upper mt-3 col-md 3">
                            
                            {% if product.PRImage %}
                            <img class="product_img" src="{{product.PRImage.url}}" alt="">
                            {% else %}
                            <img class="product_img"  src="{% static 'site_static/images/product-detail/no_image.png'%}" alt="" />
                            {% endif %}
                                
                        </div>
                        <h2><a href="">{{product.PRName}}</a></h2>
                        <div class="product-carousel-price">
                            <strong>{{product.PRPrice}} SDG</strong>

                            <!-- <ins>$899.00</ins> <del>$999.00</del> -->
                        </div>  
                        
                        <div class="product-option-shop">
                            <a class="add_to_cart_button" href="">See more Info</a>
                        </div>                       
                    </div>
                </div>
                {% endfor %}
                    
            </div>