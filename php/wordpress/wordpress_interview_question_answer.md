# Wordpress-Interview-Question-And-Answer

|  No.  | Questions                                                                                               |
| :---: | ------------------------------------------------------------------------------------------------------- |
|   1   | [What is Wordpress?](#ques-What-is-WordPress)                                                           |
|   2   | [Difference between pages and post?](#ques-Difference-between-pages-and-post)                           |
|   3   | [How many default tables are the WordPress?](#ques-How-many-default-tables-are-the-WordPress)           |
|   4   | [What is default table prefix for wordpress?](#ques-What-is-default-table-prefix-for-wordpress)         |
|   5   | [How to Create template?](#ques-How-to-Create-template)                                                 |
|   6   | [Find the path img, css & js](#ques-Find-the-path-img,-css-&-js)                                        |
|   7   | [How to call a Site title & description?](#ques-How-to-call-a-Site-title-&-description)                 |
|   8   | [How to set logo dynamically?](#ques-How-to-set-logo-dynamically)                                       |
|   9   | [How to display page content in a page template?](#ques-How-to-display-page-content-in-a-page-template) |
|  10   | [How to call widget section](#ques-How-to-call-widget-section)                                          |
|  11   | [How to disable all updates Plugin & Theme?](#ques-How-to-disable-all-updates-Plugin-&-Theme)           |
|  11   | [Author](#Author)                                                                                       |
|       | [Rearrange the admin menu](#ques-Rearrange-the-admin-menu)                                              |
|       | [Logout Redirection](#ques-logout-redirection)                                                          |


### **Ques. What Is WordPress?**
* Wordpress is a free open source content management system(CMS) written PHP language.
* It allows users to create dynamic websites from personal blogs to e-commerce.

### **Ques. Difference between pages and post?**
* Posts can be categorized vs. Pages are hierarchical.
* Posts Usually Have A Public Author, But Pages Don’t
* Posts Display In Your RSS Feed, But Pages Don’t
* Posts Have Custom “Formats”, But Pages Only Sometimes Have Templates

### **Ques. How many default tables are the WordPress?**
There are 11 table in wordpress, they are:-
* Wp_options
* Wp_links
* Wp_users
* Wp_usermeta
* wp_comments
* Wp_commentmeta
* Wp_posts
* Wp_postmeta
* Wp_terms
* Wp_term_taxonomy
* Wp_term_relationships
* Wp_termmeta  **// include new table**

### **Ques. What is default table prefix for wordpress?**
__Ans.__ wp_ is default prefix for WordPress.

### **Ques. What is the difference between the wp_title and the_title tags?**
__Ans.__ wp_tittle() function is for use outside “the Loop” to display the title of a Page. the_tittle() on the other hand is used within “the_loop“.

### **Ques. What’s the difference between site_url() and home_url()?**
__Ans.__ The site_url() will always be the location where you can reach the site by tacking on /wp-admin  on the end, while home_url() would not reliably be this location. The home_url() would be where you have set your homepage by setting genral>setting "site Address(url)" field.

### **Ques. How to Create Custom Post Type?**
__Ans.__ Custom post types are new post types you can create. A custom post type can be added to WordPress via the register_post_type() function. 

### Ques. How to Create template?
```php
<?php /* Template Name: Custom Page */ ?>
```

### Ques. How to disable new textarea?
```php
====in  functions.php========= 
add_filter('use_block_editor_for_post', '__return_false', 10);
```

### Ques. Find the path img, css & js?
```php
<link href="<?php echo get_template_directory_uri(); ?>/css/animate.min.css" rel="stylesheet">
```
* using function 
```php
wp_enqueue_style( $handle, $src, $deps, $ver, $media );
wp_enqueue_script('my_amazing_script');
```

### **Ques. How to call a Site title & description?**
```php
<?php echo esc_attr( get_bloginfo( 'name', 'display' ) ); ?>  (OR)
<?php bloginfo( 'name' ); ?> // For Site Name
<?php bloginfo( 'description' ); ?> // For Tag line or description
```

### Ques. How to set logo dynamically?
```php
<?php twentysixteen_the_custom_logo(); ?> instead of <img src="images/logo.png">
<?php the_custom_logo(); ?>

<title><?php if (is_front_page() ) { bloginfo('name'); } 
else { wp_title(''); ?> | <?php bloginfo('name'); } ?></title>

<?php bloginfo( 'description' ); ?>

<?php bloginfo('name'); ?>

<?php get_site_icon_url(); ?>

if (!has_custom_logo()) {
    ?>
    <h1><?php bloginfo('name'); ?></h1>
    <?php
}
```

### Ques. How to display page content in a page template?
```php
<?php
	while (have_posts()) : the_post();
	the_title();
	the_content();
	the_post_thumbnail();
	endwhile;
	wp_reset_postdata();
?>
```

### Ques. How to call widget section?
```php
<?php dynamic_sidebar('widget_name/widget_slug_name'); ?>
```

### Ques. How to disable all updates Plugin & Theme ?
Open the file file wp.config.php and put the code.
```sql
define('DISALLOW_FILE_MODS',true);
```

### Ques: How to Remove P and Br tags in WordPress posts? 
Open functions.php in your current active theme.<br> 
Add following lines<br>
```php
remove_filter( 'the_content', 'wpautop' ); 
remove_filter( 'the_excerpt', 'wpautop' );
```

### Ques: What is a Plugin? 
A Wordpress Plugin is a Program or a set of one or more function written in the PHP scripting language, that adds a specific language, that adds a specific set of features or services to the wordpress site.

### Ques. How to Create Child Theme?
* wp-content -> themes folder.
* twentyseventeen-child
```php
@import url('../twentyseventeen/style.css');
/* 
Theme Name: Twenty Seventeen Child 
Template: twentyseventeen 
Theme URL: http://yourdomain.com
Description: Twenty Seventeen Child 
Theme Author: Your Name
Author URL: http://yourdomain.com
Version: 1.0.0 
Text Domain: twentyseventeen-child 
*/
```

### Ques. Create Custom post Type?
```php
function slider_register_post_type()
{
$homeslider = array(
  'public' => true,
  'label' => 'job hai',
  "show_in_nav_menus" => true,
  "supports" => array( "title", "editor", "thumbnail", 'excerpt', 'comments' ),
  );
register_post_type('job', $homeslider);
}
add_action('init','slider_register_post_type');
```
```php
function hindi_register() {
    $labels = array(
        'name' => _x('Hindi', 'post type general name'),
        'singular_name' => _x('Hindi Item', 'post type singular name'),
        'add_new' => _x('Add New', 'hindi item'),
        'add_new_item' => __('Add New Hindi'),
        'edit_item' => __('Edit Hindi Item'),
        'new_item' => __('New Hindi Item'),
        'view_item' => __('View Hindi Item'),
        'search_items' => __('Search Hindi Items'),
        'not_found' =>  __('Nothing found'),
        'not_found_in_trash' => __('Nothing found in Trash'),
        'parent_item_colon' => ''
    );
    $args = array(
        'labels' => $labels,
        'public' => true,
        'menu_icon'   => 'dashicons-format-gallery',
        'publicly_queryable' => true,
        'show_ui' => true,
        'query_var' => true,
        'rewrite' => true,
        'capability_type' => 'post',
        'hierarchical' => false,
        'menu_position' => 8,
        'supports' => array('title','editor','thumbnail')
    ); 
    register_post_type( 'hindi' , $args );
}
add_action('init', 'hindi_register');
function create_hindi_taxonomies() {
    $labels = array(
        'name'              => _x( 'Categories', 'taxonomy general name' ),
        'singular_name'     => _x( 'Category', 'taxonomy singular name' ),
        'search_items'      => __( 'Search Categories' ),
        'all_items'         => __( 'All Categories' ),
        'parent_item'       => __( 'Parent Category' ),
        'parent_item_colon' => __( 'Parent Category:' ),
        'edit_item'         => __( 'Edit Category' ),
        'update_item'       => __( 'Update Category' ),
        'add_new_item'      => __( 'Add New Category' ),
        'new_item_name'     => __( 'New Category Name' ),
        'menu_name'         => __( 'Categories' ),
    );

    $args = array(
        'hierarchical'      => true, // Set this to 'false' for non-hierarchical taxonomy (like tags)
        'labels'            => $labels,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array( 'slug' => 'categories' ),
    );

    register_taxonomy( 'hindi_categories', array( 'hindi' ), $args );
}
add_action( 'init', 'create_hindi_taxonomies', 0 );
```

### Ques. How to fetch data from a custom post type?
```php
<?php $args = array('post_type' => 'slider','posts_per_page'=>-1,'post_status' => 'publish',
		'category_name' => 'mobile_apps', 'order' => 'DESC',
		'product_cat' => '3-d-photo-popouts-with-background');
            $loop = new WP_Query( $args );
      	while ( $loop->have_posts() ) : $loop->the_post();?>
      	<?php $i = 1; while (have_posts() && $i < 6) : the_post(); ?>

      		
	<?php $i++; endwhile; ?>
	<?php endwhile; ?>


<img src="<?php echo wp_get_attachment_url( get_post_thumbnail_id( $post->ID ));?>" class="about-ion-top_img"/>
<?php echo the_post_thumbnail( array(70, 70, true) ); ?>  //img src nahi lagega
<?php echo the_post_thumbnail( 'thumbnail' ); ?>
<?php the_post_thumbnail('thumbnail', array('class' => 'img-responsive img-circle')); ?>
<?php echo get_the_post_thumbnail( $post_id, 'thumbnail', array('class' => 'img-responsive img-circle')); ?>

        	<?php
               if( has_post_thumbnail() ) {
                //Add in featured image & class
                the_post_thumbnail( 'medium', array( 'class' => 'img-responsive' ) ); 
               } else{ 
            ?>
<img src="<?php bloginfo('template_directory'); ?>/images/blog-default-image.png" class="img-responsive" 
									alt="Blog Default Image">   
            <?php  
        		} 
        	?>

        	title="<?php the_title_attribute(); ?>"
        	<?php echo $post->post_title ?>
        	<?php echo $post->post_content ?>
        	<?php echo substr($post->post_content, 0, 150);  ?>
        	<?php echo get_the_time( 'F j, Y', $post->ID ) ?>
        	<a href="<?php echo get_permalink( $post->ID ); ?>">
        	<?php the_time(); ?>
            <?php the_tags(); ?>
            <?php next_posts_link(); ?>
            <?php previous_posts_link(); ?>
            <?php the_post_thumbnail(); ?>
            <?php the_excerpt(); ?>
            <?php comment_form(); ?>
            <?php comments_popup_link('No Comments ', '1 Comment ', '% Comments '); ?>
	<?php echo timeago(); ?>
<?php echo human_time_diff(get_the_time('U'), current_time('timestamp')) . ' ago'; ?>

<section class="inn-pagebanner" style="background-image: url('<?php echo wp_get_attachment_url
		( get_post_thumbnail_id( $post->ID ) ); ?>'); background-position: center;">
```


### Ques. What is a WordPress taxonomy ?
In WordPress, a “taxonomy” is a grouping mechanism for some posts (or links or custom post types).<br>
There are four default taxonomies in WordPress they are-<br>
* Category
* Tag
* Link Category
* Post Formats

### Ques. What are the types of hooks in WP and what are their functions ?
__Action Hooks:-__
* We can add new css and js by action hooks.
* An Action hook in WordPress is a hook that is triggered at a specific time when WordPress is running and lets you take action.
* Doing something new. Ex:- adding css and js

###### Below are list of some Action hooks functions:-
* has_action()
* add_action()
* do_action()
* do_action_ref_array()
* did_action()
* remove_action()
* remove_all_actions()
* doing_action()

__Filter Hooks:-__
* A Filter hook in WordPress allows you to get and modify WordPress data before it is sent to the database or the browser.
* Doing something which is already in wordpress. 
###### Below are list of some Filter hooks functions:-
* has_filter()
* add_filter()
* apply_filters()
* apply_filters_ref_array()
* current_filter()
* remove_filter()
* remove_all_filters()
* doing_filter()

add_filter('use_block_editor_for_post', '__return_false');

 
### How do you enable debug mode in WP?
You can enable __debug mode__ in WP by editing __wp-config.php__ file and changing __WP_DEBUG__ constant value to __true__.
 
### Ques. How to create a folder if it doesn't already exist in Wordpres?
```php
$pathname='path/to/directory'; 
if (!file_exists($pathname)) {    
mkdir($pathname, 0777, true); 
}
__Pathname:__ path where you want to create the folder Folder 
__Permission:__ Permission of folder. 
__Recursive:__ true for all sub directory, false for current directory only. 
```

### Ques. What is difference between mode value 0777 and 777 in mkdir/chmod function? 
In PHP, 0777 and 777 have same meaning and no difference.<br>When you are providing 4 digit in for permission, it means 1 digit will be used for sticky bit. <br>
__sticky bit__ is access right flag that can be assigned to files and directories on Unix-like systems.

### Ques: Where to place to insert the google analytics Code? 
You should add "Google analytics code" in Every page, so that you can get all pages tracking report. As per google, you should add "Google Analytics code" just before the closing of "head" for better results.<br>In wordpress, when we are using some theme for displaying your website. there might be textbox in admin section, to add the "Google Analytics" code for tracking purpose. (May OR may not available in your current theme)

### Ques: How to get the current page name in WordPress? You can get the page name from below of two? 
```php
$slug = basename(get_permalink());
OR
$pagename = get_query_var('pagename'); 
```

### Ques: How do I ge the version of wordpress?
```php
echo bloginfo('version');
OR
Above is get from below file. You can check in wp-includes/version.php  
$wp_version = '4.1.2';
```

### Ques: How to turn off the Notice/Warning from my wordpress website? 
Open the wp-config.php file and WP_DEBUG set the false.
```php
define('WP_DEBUG', false );
```

### Ques: What is use of __() and _e() functions in wordpress? 
These are function used when you website multilingual. each of this function have two parameter.<br>
1st parameter: String which you want to convert from one language to another.<br>
2nd parameter: domain name.<br>
```php
 $translatedText = __( 'TEXT_FOR_TRANSLATION', 'textdomain' ); //This will return the translated text 
 _e( 'TEXT_FOR_TRANSLATION', 'textdomain' ); //This will print the translated text
 ```

 ### Ques: How to get wordpress post featured image URL?
```php
if (has_post_thumbnail( $post->ID ) ){   
$image = wp_get_attachment_image_src( get_post_thumbnail_id( $post->ID ), 'single-post-thumbnail' );  
echo $image[0];//image url 
}
```

### Ques: How to get last inserted row id from wordpress database?
```php
global $wpdb; 
/** insert query here with $wpdb**/ 
/** insert query here with $wpdb**/ 
$lastId = $wpdb->insert_id; //This is last insert id
```

### Ques: How do I get current taxonomy "term id" on wordpress?
```php
$obj = get_queried_object(); 
echo $obj->term_id;
```

### Ques: How do I add Syntax Highlighting on wordpress.com? 
As you can't install plugin for syntax high lighting in wordpress.com, you can use existing syntax highligher.  
```php
[sourcecode language='python']
[/sourcecode]
```

### Ques: How to check admin login or Not?
```php
if(is_admin()) { 
/** Write your code here */
/** Write your code here */ 
}
```

### Ques. How to protect your website from DDos Attack? 
Add following code in your .htaccess file. 
```php
<files xmlrpc.php>      
order allow,deny       
deny from all     
</files>
```
 
### Ques: Logout Redirection?
```php
==========function.php============
add_action('wp_logout','ms_redirect_after_logout');
function ms_redirect_after_logout(){
         wp_redirect( home_url() );
         exit();
}
```

### Logout Link
```php
http://mywebsitenamehere.com/wp-login.php?action=logout
http://www.website.com/?customer-logout=true
```

### Ques. Displaying Logged-In User Name in Wordpress Menu?
```
=============Apprence-> menu-> custom_link.=====================
 #profile_name# 
```
```php
==============function.php============
function give_profile_name($atts){
    $user=wp_get_current_user();
    $name=$user->user_firstname; 
    return $name;
}

add_shortcode('profile_name', 'give_profile_name');

add_filter( 'wp_nav_menu_objects', 'my_dynamic_menu_items' );
function my_dynamic_menu_items( $menu_items ) {
    foreach ( $menu_items as $menu_item ) {
        if ( '#profile_name#' == $menu_item->title ) {
            global $shortcode_tags;
            if ( isset( $shortcode_tags['profile_name'] ) ) {
                // Or do_shortcode(), if you must.
                $menu_item->title = call_user_func( $shortcode_tags['profile_name'] );
            }    
        }
    }

    return $menu_items;
} 
```
### Ques. Rearrange the admin menu?
```php
 // Rearrange the admin menu
  function custom_menu_order($menu_ord) {
    if (!$menu_ord) return true;
    return array(
      'index.php', // page
      'edit.php?post_type=slider', // Custom type one
    );
  }

  add_filter('custom_menu_order', 'custom_menu_order'); // Activate custom_menu_order
  add_filter('menu_order', 'custom_menu_order');
```

================================
 <?php $i++;
            if($i==3){ ?> <div class="clearfix"></div>
           <?php $i=0; } ?>

=============================
<div class="rating-star">
        <?php 
 $rat = get_post_meta($post->ID, 'rating', true); 

for($i=1; $i<=5; $i++){
 if($rat>=$i){

echo '<i class="fa fa-star yellow" aria-hidden="true"></i> ';
}
else{
echo '<i class="fa fa-star " aria-hidden="true"></i> ';
}
}
?>              
</div>

### Header Menu 
```php
<?php
     $args = wp_nav_menu(array(
       'menu_class' => 'nav navbar-nav right chevron',     
        'menu'       => '(header-menu)'
         ));
       ?>
       
<?php
  wp_nav_menu( array(
  'menu' => 'menu-nav',
   'items_wrap' => '<ul class="nav navbar-nav">%3$s</ul>',
     ) );
?>
              
<?php
  wp_nav_menu( array(
  'theme_location' => 'primary',
   'items_wrap' => '<ul>%3$s</ul>',
    'container' => 'ul',
   'menu_id' => 'cssmenu',
    'depth' => '2'
   ) );
?>

<?php $defaults = array(
  'theme_location'  => ,
  'menu'          => 'menu-nav',
   'container'    => 'div',
  'container_class' => 'menu-{menu slug}-container',
  'container_id'  => ,
  'menu_class'    => 'menu',
  'menu_id'       => ,
  'echo'          => true,
  'fallback_cb'   => 'wp_page_menu',
  'before'        => ,
  'after'         => ,
  'link_before'   => ,
  'link_after'    => ,
  'items_wrap'    => '<ul id=\"%1$s\" class=\"%2$s\">%3$s</ul>',
  'depth'         => 0,
  'walker'        => );
?>
```
 
### Advanced Custom Fields(https://wordpress.org/plugins/advanced-custom-fields/) 
```php
<?php the_field("service_work_process",8); ?>

<img src="<?php
 $appl1 = get_field("apIMG2" ,4);
echo $appl1['url']; ?>" alt="" />
```

=========================================================================
slider ko dynamic banane ke liye......
=========================================================================
<?php
global $wp;
$current_url =  home_url( $wp->request ); 
$url = site_url().'/treinamentos-tech-consulting';
if($current_url == $url){?>

============
if ( is_front_page() ) {
}
<ul class="slides">
       <?php
       global $post;
       $args = array( 'offset'=> 0, 'category' => 3 ); // category id admin sa chek karna hai
       $myposts = get_posts( $args );
       foreach ( $myposts as $post ) :  
       ?>
       <li>
       <div class="banner-info1">
         <h3><?php echo $post->post_content ?></h3>
           </div>
        </li>
       <?php endforeach;
       wp_reset_postdata(); ?>
</ul>
===============

====================================
<?php
            $icon = array('icon-flag','icon-clock', 'icon-hotairballoon', 'icon-heart', 'icon-linegraph', 'icon-chat');
            $args = array('post_type' => 'chooseus','posts_per_page'=>-1,'post_status' => 'publish');

            $loop = new WP_Query( $args );
            $i='0';
      while ( $loop->have_posts() ) : $loop->the_post();?>
<div class="col-sm-6 col-md-4 col-lg-4">
          <div class="alt-features-item align-center">
              <div class="alt-features-icon">
                  <span class="<?php echo $icon[$i];?>"></span>
              </div>
                  <h3 class="alt-features-title font-alt"><?php echo $post->post_title ?></h3>
              <div class="alt-features-descr align-left">
              <?php echo $post->post_content ?>
              </div>
          </div>
      </div>
      <?php $i++;endwhile; ?>




### function mai array banya dropdown ka... phir page par call karya
```php
function priceList()
{
  return $priceList = array('Any','50000','100000','150000','200000','250000','300000','350000','400000' ,'450000','500000','550000','600000','650000','700000','750000','800000','850000','900000','950000','1000000','1250000','1500000','1750000','2000000','2500000','3000000','4,000,000','5,000,000','10,000,000');
}

 <select class="form-control price" type="text" name="search_max_price" id="search_max_price">
          <option value="" >Max Price</option>
        <?php $priceListValue = priceList();  
                foreach($priceListValue as $valList){?>
          <option value="<?php echo $valList;?>">$ <?php echo $valList;?></option>
          <?php }?>
        </select>
```

wp
<select name="destination" class="wpcf7-form-control wpcf7-select form-control" id="destination" aria-invalid="false">
            <option value="India" <?php echo ucfirst($lastword)=='India'?'selected':'';?>>India</option>
            <option value="Bhutan" <?php echo ucfirst($lastword)=='Bhutan'?'selected':''; ?>>Bhutan</option>
            <option value="Nepal" <?php echo ucfirst($lastword)=='Nepal'?'selected':''; ?>>Nepal</option>
            <option value="Sri Lanka" <?php echo ucfirst($lastword)=='Sri-lanka'?'selected':''; ?>>Sri Lanka</option>
            <option value="Maldives" <?php echo ucfirst($lastword)=='Maldives'?'selected':'';?>>Maldives</option>
            <option value="Tibet" <?php echo ucfirst($lastword)=='Tibet'?'selected':'';?>>Tibet</option>           
        </select>

         <?php  
                for($i=0; $i<count($location); $i++){
                  $selected=ucfirst($lastword)==$location[$i]?'selected':'';
                  echo '<option value="'.$location[$i].'" '.$selected.'>'.getStrToUpper($location[$i]).'</option>';  

                  ?>
             
          <?php }?>

///<?php echo do_shortcode( '[contact-form-7 id="27" title="Contact form 1"]' ); ?>



###  alternet loop
```php
<?php $args = array('post_type' => 'profiles','posts_per_page'=>-1,'post_status' => 'publish');           
$loop = new WP_Query( $args );
$i=0;
while ( $loop->have_posts() ) : $loop->the_post();
if($i%2==0){?>
   // Some Code
<?php }else{?>
   // Some Code
<?php } $i++;?>
<?php endwhile; ?>
```


==============================================================
<div class="col-sm-8 col-sm-offset-2">
  <div class="align-center mb-40 mb-xxs-30">
      <ul class="nav nav-tabs tpl-minimal-tabs animate">
          <li class="active">
              <a href="#mini-one" data-toggle="tab">Mission</a>
          </li>
          <li>
              <a href="#mini-two" data-toggle="tab">Vision</a>
          </li>
          <li>
              <a href="#mini-three" data-toggle="tab">Ideas</a>
          </li>
      </ul>
  </div>
  <div class="tab-content tpl-minimal-tabs-cont section-text align-center">
      <div class="tab-pane fade in active" id="mini-one">
          Mission-To be a most preferred quality software developmentand Resourcing Partner throughout the world by providing quality services.
      </div>
      <div class="tab-pane fade" id="mini-two">
          To be a successful service Oriented company globally by meet or exceed our customer needs and expectations by delivering cost effective, right quality and customer oriented technology solutions on time.
      </div>
      <div class="tab-pane fade" id="mini-three">
          Attach with DNA App Store, an online store for information about your genes will make it cheap and easy to learn more about your health risks and predispositions.
      </div>
  </div>
</div>
============================================================
<div class="col-sm-8 col-sm-offset-2">
  <?php $args = array('post_type' => 'ourstory','posts_per_page'=>-1,'post_status' => 'publish');

            $loop = new WP_Query( $args );?>
      <!-- Nav Tabs -->
      <div class="align-center mb-40 mb-xxs-30">
          <ul class="nav nav-tabs tpl-minimal-tabs animate">
              <?php $i='1';while ( $loop->have_posts() ) : $loop->the_post();?>
                  <li class="<?php if($i=='1'){?>active<?php }?>">
                      <a href="#<?php echo $i;?>" data-toggle="tab"><?php echo $post->post_title ?></a>
                  </li>
                  <?php $i++;endwhile;?>
          </ul>
      </div>
      <div class="tab-content tpl-minimal-tabs-cont section-text align-center">
          <?php $j='1';while ( $loop->have_posts() ) : $loop->the_post();?>
              <div class="tab-pane fade in <?php if($j=='1'){?>active<?php }?>" id="<?php echo $j;?>">
                  <?php echo $post->post_content; ?>
              </div>
              <?php $j++;endwhile;?>
      </div>
</div>
=================
 <?php
  global $post;
  $args = array( 'post_type' => 'health','category_name' => 'health-adver');
  $myposts = get_posts( $args );
  $i='1';
  foreach ( $myposts as $post ) :?>
  <p><?php echo $i;?>) <a href="<?php echo get_permalink( $post->ID ); ?>"><?php echo substr($post->post_title, 0, 70);  ?>..</a></p>
  <?php $i++;endforeach;
    wp_reset_postdata(); ?>
    =======================================
    <?php echo $product->get_price_html(); ?>
    <?php woocommerce_template_loop_add_to_cart($loop->post, $product ); ?>


 ### insert data in wordpress
 ```php
  <?php
  get_header(); 
  if(isset($_POST["submit"])){
        global $wpdb;
        print_r($_POST);
        $positions = $_POST["positions"];
        $fname = $_POST["fname"];      
       
        $sql = "INSERT INTO `apply_now_form`(`positions`, `name`) VALUES ('$positions','$fname')";

        if($wpdb->query($sql)){
          echo "Success Fully Insert.";          
        }else{
          echo "Insert Error ...";
        }
        }
```
__When also Mail sent__
```php
$sql = "INSERT INTO `apply_now_form`(`positions`, `name`) VALUES ('$positions','$fname')";
        
$wpdb->query($sql);          
$to   = 'mksaxena27@gmail.com';
$to = array(
   	'recipient1@example.com',
   	'recipient2@foo.example.com'
	);
$subject = $_POST["fname"];
$message = "<b>Name = </b>".$_POST["fname"]."<br><br>"."<b>Email = </b>".$_POST["email"]."<br><br>".
            "<b>Phone = </b>".$_POST["phone"]."<br><br>"."<b>State = </b>".$_POST["state"]."<br><br>";
$headers = array('Content-Type: text/html; charset=UTF-8');
if(wp_mail( $to, $subject, $message, $headers ))
 {
  echo "<p style=' width: 90%; border: solid 1px #ccc; border-radius: 5px;
                    padding: 4px;  margin-top: 10px; color: #2e7ebe;'>Your mail is successfully sent</p>";
  }else{
      echo "Failed";
  }
   ?>
```
### After 3 Post Clearfix
```php
 <?php $i++; if($i==3){ ?> <div class="clearfix"></div> <?php $i=0; } ?>
```
### Default editior
```php
add_filter('use_block_editor_for_post', '__return_false');
```
### rating Star
```php
<div class="rating-star">
<?php 
$rat = get_post_meta($post->ID, 'rating', true); 
for($i=1; $i<=5; $i++){
if($rat>=$i){
echo '<i class="fa fa-star yellow" aria-hidden="true"></i> ';
}
else{
echo '<i class="fa fa-star " aria-hidden="true"></i> ';
}
}
?>           
</div>
```
### if Condtion
```php
<?php if (is_page(20) ){?> <?php } ?>
<?php if( $post->ID == 172) { ?> <?php } ?>
```

<form action="#" method="post">
   <div>
  <label for="recieved-date">Date Recieved:</label>
  <input type="date" name="" id="recieved-date" disabled class="form-control">
   </div>
  <input type="submit" id="signature" class="btn btn-info" name="submit" value="Submit">
 
++++++++++++++
<?php
+++++++++++++++++ 
function remove_from_wordpress($email){
$wpfrom = get_option('blogname');
return $wpfrom;
}


function wpb_sender_email( $original_email_address ) {
    return 'tim.smith@example.com';
}
 
// Function to change sender name
function wpb_sender_name( $original_email_from ) {
    return 'Tim Smith';
}
 
// Hooking up our functions to WordPress filters 
add_filter( 'wp_mail_from', 'wpb_sender_email' );
add_filter( 'wp_mail_from_name', 'wpb_sender_name' );
++++++++++++++++++++++++++++++++++

function codecanal_mail_from_name($old) {
    $site_name = get_option( 'blogname');
    return $site_name;
}
 

add_filter('wp_mail_from', 'codecanal_mail_from');
function codecanal_mail_from($old) {
    $email = get_option( 'admin_email' );
    return $email;
  }


  add_filter('wp_mail_from', 'codecanal_mail_from');
function codecanal_mail_from($old) {
    return 'admin@example.com';
    /* replace "admin@example.com" with your desired email address */
}

?>


<?php function Faqs_function() { ?>  
<h1>mohit</h1>
<?php }
?>
<?php add_shortcode('lorem', 'Faqs_function'); ?>

/=================================================

----------------------
function wpbsearchform( $form ) {
 
    $form = '<form role="search" method="get" id="searchform" action="' . home_url( '/' ) . '" >
    <div>
    <input type="text" value="' . get_search_query() . '" name="s" id="s" />
    <input type="submit" id="searchsubmit" value=" '. esc_attr__('Search') .'" />
    </div>
    </form>';
 
    return $form;
}
 
add_shortcode('wpbsearch', 'wpbsearchform');

<?php //echo do_shortcode( '[wpbsearch]' ); ?>
======================================================
Pagination
===============================
<?php
the_posts_pagination( array(
            'prev_text'          => __( '<<', 'twentysixteen' ),
                'next_text'          => __( '>>', 'twentysixteen' ),
                'screen_reader_text' => __('&nbsp;', 'twentysixteen')
               // 'before_page_number' => '<span class="meta-nav screen-reader-text">' . __( 'Page', 'twentysixteen' ) . ' </span>',
            ) );
?>         
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

=====================================
  category image display
  <?php foreach (get_categories() as $cat) : ?>

<img src="<?php echo z_taxonomy_image_url($cat->term_id); ?>" />
<a href="<?php echo get_category_link($cat->term_id); ?>"><?php echo $cat->cat_name; ?></a>

<?php endforeach; ?>
=========================================================
<?php echo human_time_diff(get_the_time('U'), current_time('timestamp')) . ' ago'; ?> // 2 days ago


function timeago( $type = 'post' ) {
    $d = 'comment' == $type ? 'get_comment_time' : 'get_post_time';
    return human_time_diff($d('U'), current_time('timestamp')) . " " . __('ago');
}


<?php echo timeago(); ?>
========================================================

blog page++++++++++++++++
<?php echo the_post_thumbnail( array(60, 60, true) ); ?> 
tage show---------
           <div class="entry-tags">
                      <span>Tags: </span>
                    <?php $tags = get_tags(); ?>
<div class="tags">
<?php foreach ( $tags as $tag ) { ?>
    <a href="<?php echo get_tag_link( $tag->term_id ); ?> " rel="tag"><?php echo $tag->name; ?></a>
<?php } ?>
</div>
</div>

Disable All Update Notifications:
Insert Code In Function.php:-

function remove_core_updates(){
    global $wp_version;return(object) array('last_checked'=> time(),'version_checked'=> $wp_version,);
}
add_filter('pre_site_transient_update_core','remove_core_updates');
add_filter('pre_site_transient_update_plugins','remove_core_updates');
add_filter('pre_site_transient_update_themes','remove_core_updates');





Post show state wise:-
<form class="filter-frm" action="" method="post">
        <div class="col-sm-2">  <label>State:</label> </div>
        <div class="col-sm-3">
          <select name="state" id="state">
            <option value="" >--Select State--</option>
            <?php 
              $query = "SELECT * FROM states ORDER BY id ASC";              
              $result = mysqli_query($conn, $query);  
              while($row = mysqli_fetch_array($result))  
              {    
              ?>  
               <option value="<?php echo $row["StateName"]; ?>" <?php echo $row["StateName"]==$_REQUEST['state']?'selected="selected"':''; ?>> <?php echo $row["StateName"]; ?></option>                               
               <?php } ?>
            </select>
        </div>
        <div class="col-sm-2">
          <input type="submit"  class="btn btn-primary" value="Submit" name="submit"/>
        </div>
        <div class="clearfix"></div>
      </form>
-----------------------------------------------------------------------
<?php $args = array('post_type' => 'gallery','posts_per_page'=>-1,'post_status' => 'publish','gallery_categories'=>isset($_REQUEST['state'])?$_REQUEST['state']:'');
        $loop = new WP_Query( $args );
            while ( $loop->have_posts() ) : $loop->the_post();?>


Create custom admin bar menu items:
function custom_adminbar_menu( $meta = TRUE ) {
    global $wp_admin_bar;
        if ( !is_user_logged_in() ) { return; }
        if ( !is_admin_bar_showing() ) { return; }
    $wp_admin_bar->add_menu( array(
        'id' => 'custom_menu',
        'title' => __( '<span class="lifemx ab-icon"></span>Magazine' ) )
    );
  $wp_admin_bar->add_menu( array(
    'parent'    => 'custom_menu',
    'title'     => '<span class="lifemm ab-icon"></span>My posts',
    'href'  => '/wp-admin/edit.php'
   )
  );
    $wp_admin_bar->add_menu( array(
        'parent'    => 'custom_menu',
        'title'     => '<span class="lifemm ab-icon"></span>Home Page',
        'href'  => '/lifestyle/',
        'meta'  => array( target => '_blank' ) )
    );
}
add_action( 'admin_bar_menu', 'custom_adminbar_menu', 15 );


How to call comment in template page:


  <?php
$args = array(
    'status' => 'approve',
    'posts_per_page'=>1
);
 
// The comment Query
$comments_query = new WP_Comment_Query;
$comments = $comments_query->query( $args ); 
// Comment Loop
if ( $comments ) {
    foreach ( $comments as $comment ) { ?>    
      <div class="testi-item">
<img src="<?php echo get_template_directory_uri(); ?>/images/noimage.png" />
                          <h5><?php   echo $comment->comment_author ?> </h5>
                          <p><?php echo $comment->comment_content; ?></p>
                          <a href="<?php get_comment_author_link(); ?>"> Read more </a>
                        </div>
      <?php
    }
} else {   echo 'No comments found.'; }
?>

Breadcrumb :
<ul> <li><a href="<?php echo home_url(); ?>/projects">Projects</a></li> <?php $term = get_term_by("slug", get_query_var("term"), get_query_var("taxonomy") ); $tmpTerm = $term; $tmpCrumbs = array(); while ($tmpTerm->parent > 0){ $tmpTerm = get_term($tmpTerm->parent, get_query_var("taxonomy")); $crumb = '<li><a href="' . get_term_link($tmpTerm, get_query_var('taxonomy')) . '">' . $tmpTerm->name . '</a></li>'; array_push($tmpCrumbs, $crumb); } echo implode('', array_reverse($tmpCrumbs)); echo '<li><a href="' . get_term_link($tmpTerm, get_query_var('taxonomy')) . '">' . $term->name . '</a></li>'; ?> </ul>
========================================
  <?php
/*
Credit goes to Dominic Barnes - http://stackoverflow.com/users/188702/dominic-barnes
http://stackoverflow.com/questions/2594211/php-simple-dynamic-breadcrumb
*/
// This function will take $_SERVER['REQUEST_URI'] and build a breadcrumb based on the user's current path
function breadcrumbs($separator = ' &raquo; ', $home = 'Home') {
    // This gets the REQUEST_URI (/path/to/file.php), splits the string (using '/') into an array, and then filters out any empty values
    $path = array_filter(explode('/', parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH)));
    // This will build our "base URL" ... Also accounts for HTTPS :)
    $base = ($_SERVER['HTTPS'] ? 'https' : 'http') . '://' . $_SERVER['HTTP_HOST'] . '/';
    // Initialize a temporary array with our breadcrumbs. (starting with our home page, which I'm assuming will be the base URL)
    $breadcrumbs = Array("<a href=\"$base\">$home</a>");
    // Find out the index for the last value in our path array
    $last = end(array_keys($path));
    // Build the rest of the breadcrumbs
    foreach ($path AS $x => $crumb) {
        // Our "title" is the text that will be displayed (strip out .php and turn '_' into a space)
        $title = ucwords(str_replace(Array('.php', '_'), Array('', ' '), $crumb));
        // If we are not on the last index, then display an <a> tag
        if ($x != $last)
            $breadcrumbs[] = "<a href=\"$base$crumb\">$title</a>";
        // Otherwise, just display the title (minus)
        else
            $breadcrumbs[] = $title;
    }
    // Build our temporary array (pieces of bread) into one big string :)
    return implode($separator, $breadcrumbs);
}
?>
<?php
// Default options - Home » Page Title
echo breadcrumbs() ;
// Change » to >
// echo breadcrumbs(' > '); 
// Change 'Home' to 'Index' and » to ^^
// echo breadcrumbs(' ^^ ', 'Index');
?>


Category Description in html formet :

foreach ( array( 'pre_term_description' ) as $filter ) { 
    remove_filter( $filter, 'wp_filter_kses' ); 
} 
foreach ( array( 'term_description' ) as $filter ) { 
    remove_filter( $filter, 'wp_kses_data' ); 
} 







=================
 <?php
  global $post;
  $args = array( 'post_type' => 'health','category_name' => 'health-adver');
  $myposts = get_posts( $args );
  $i='1';
  foreach ( $myposts as $post ) :?>
  <p><?php echo $i;?>) <a href="<?php echo get_permalink( $post->ID ); ?>"><?php echo substr($post->post_title, 0, 70);  ?>..</a></p>
  <?php $i++;endforeach;
    wp_reset_postdata(); ?>
    =======================================
    <?php echo $product->get_price_html(); ?>
    <?php woocommerce_template_loop_add_to_cart($loop->post, $product ); ?>

  

  

   ?>
   <form action="#" method="post">
   <div>
  <label for="recieved-date">Date Recieved:</label>
  <input type="date" name="" id="recieved-date" disabled class="form-control">
   </div>
  <input type="submit" id="signature" class="btn btn-info" name="submit" value="Submit">
 
++++++++++++++
<?php
+++++++++++++++++ 
function remove_from_wordpress($email){
$wpfrom = get_option('blogname');
return $wpfrom;
}


function wpb_sender_email( $original_email_address ) {
    return 'tim.smith@example.com';
}
 
// Function to change sender name
function wpb_sender_name( $original_email_from ) {
    return 'Tim Smith';
}
 
// Hooking up our functions to WordPress filters 
add_filter( 'wp_mail_from', 'wpb_sender_email' );
add_filter( 'wp_mail_from_name', 'wpb_sender_name' );
++++++++++++++++++++++++++++++++++

function codecanal_mail_from_name($old) {
    $site_name = get_option( 'blogname');
    return $site_name;
}
 

add_filter('wp_mail_from', 'codecanal_mail_from');
function codecanal_mail_from($old) {
    $email = get_option( 'admin_email' );
    return $email;
  }


  add_filter('wp_mail_from', 'codecanal_mail_from');
function codecanal_mail_from($old) {
    return 'admin@example.com';
    /* replace "admin@example.com" with your desired email address */
}

?>



<?php function Faqs_function() { ?>  
<h1>mohit</h1>
<?php }
?>
<?php add_shortcode('lorem', 'Faqs_function'); ?>

### Ques. How to call shortcode?
```php
<?php echo do_shortcode( '[contact-form-7 id="27" title="Contact form 1"]' ); ?>
```

### Ques. particular page ke liye 
```php
<?php if(is_page('projects')|| is_page('to-qualify')):?>
  // Some Code
<?php endif; ?>
---------------------------------------
if(!is_page('about-us')){
get_sidebar();
} 
<?php if(!is_page('next/ID'))
{
dynamic_sidebar( 'sidebar-2' );   
}
```

### Create Widget
```php
class my_first_widgt extends wp_widget
{
  function __construct(){
    parent::__construct(false, $name = __('MY FIRST widget'));
  }
  function widget($args, $instance){ ?>

  plz write html code here
<?php
  }
}
add_action('widgets_init',function(){
  register_widget('my_first_widgt');
});
```

# Blog Page

### Post Show
```php
<?php $args = array('post_type' => 'post','posts_per_page'=>3,'post_status' => 'publish','paged' => get_query_var('paged') ? get_query_var('paged') : 1);
  $loop = new WP_Query( $args );
   while ( $loop->have_posts() ) : $loop->the_post();?>

Comment: <?php echo $post->comment_count; ?>
view: <?php echo getPostViews(get_the_ID()); ?>
view <?php echo setPostViews(get_the_ID()); ?>
Days Ago: <?php echo human_time_diff(get_the_time('U'), current_time('timestamp')) . ' ago'; ?>
Auther: <a href="<?php echo get_author_posts_url( get_the_author_meta( 'ID' ) ); ?>"><?php echo get_the_author(); ?></a><br>
image: <?php echo the_post_thumbnail( array(70, 70, true) ); ?> 
<!-- image: <img src="<?php echo wp_get_attachment_url( get_post_thumbnail_id( $post->ID ));?>" />     		 -->
     		<br><br>          
<?php endwhile; ?>
 <ul class="pagination">       
<?php
$big = 999999999; // need an unlikely integer
 echo paginate_links( array(
    'base' => str_replace( $big, '%#%', get_pagenum_link( $big ) ),
    'format' => '?paged=%#%',
    'current' => max( 1, get_query_var('paged') ),
    'total' => $loop->max_num_pages
) );
?>
 </ul>
 ```

### Search box on blog page
```php
<form role="search" method="get" id="searchform" class="searchform" 
	action="<?php echo esc_url( home_url( '/' ) ); ?>"><div>
<label class="screen-reader-text" for="s">Search for:</label>
<input type="text" value="" name="s" id="s" />
<input type="submit" id="searchsubmit" value="Search" />
</div>
</form>
```

### Author
```php
<p>Written by: <?php the_author_posts_link(); ?></p>

<h2>List of authors:</h2>
<ul>
<?php //wp_list_authors(); ?>
<?php wp_list_authors('exclude_admin=0'); ?>
</ul>
```

### Ques. How to fetch categories in a blog page ?
```sql 
<?php 		  
	$args = array(
	'orderby'    => 'ID', 
	'order'      => 'ASC',
	'hide_empty' => false
	);
	$tax_terms = get_terms('category', $args);
?>
<?php foreach($tax_terms as $term_single) { ?>
<a href="<?php echo home_url();?>/category/<?php echo $term_single->slug; ?>"><?php echo $term_single->name; ?> <span>(<?php echo $term_single->count; ?>)</span></a>
<a href="<?php echo get_category_link($term_single->term_id); ?>"><?php echo $term_single->name; ?></a>
<?php echo $term_single->count; ?>
<?php echo $term_single->description; ?>
<?php } ?>  (OR)

<?php 
$categories = get_categories( array(
    'orderby' => 'name',
    'order'   => 'ASC'
) );
 
foreach( $categories as $category ) { ?>
  <a href="<?php echo get_category_link($category->term_id); ?>"><?php echo $category->name; ?></a> 
  <?php
} ?>
```

### Ques. How to fetch Tag in blog page ?
```sql 
<?php $tags = get_tags(); ?>

<?php foreach ( $tags as $tag ) { ?>
<a href="<?php echo get_tag_link( $tag->term_id ); ?> " rel="tag"><?php echo $tag->name; ?></a>
<?php } ?>
```
	
### Show The Product Image In Checkout Page.
```php
/*
 * Show The Image In Checkout Page.
 */

add_filter( 'woocommerce_cart_item_name', 'ts_product_image_on_checkout', 10, 3 ); 
function ts_product_image_on_checkout( $name, $cart_item, $cart_item_key ) {
     
    /* Return if not checkout page */
    if ( ! is_checkout() ) {
        return $name;
    }
     
    /* Get product object */
    $_product = apply_filters( 'woocommerce_cart_item_product', $cart_item['data'], $cart_item, $cart_item_key );
 
    /* Get product thumbnail */
    $thumbnail = $_product->get_image();
 
    /* Add wrapper to image and add some css */
    $image = '<div class="ts-product-image" style="width: 52px; height: 45px; display: inline-block; padding-right: 7px; vertical-align: middle;">'
                . $thumbnail .
            '</div>'; 
 
    /* Prepend image to name and return it */
    return $image . $name;
}
```
	

### language changing in drop down
```php
    <script type="text/javascript">
function googleTranslateElementInit() {
new google.translate.TranslateElement({pageLanguage: 'en',includedLanguages: 'en,es,zh',  layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}
</script>
<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit">
</script>
  <div id="google_translate_element"></div>
  <style type="text/css">
  .goog-te-banner-frame.skiptranslate {display: none !important;}
  body { top: 0px !important; }
  img.goog-te-gadget-icon {
  display: none;
}
.goog-te-gadget-simple {
border-radius: 3px;
margin-left: 7px;
}
  </style>
```
### form update and image update in databse and folder 
```php
if(isset($_POST['Updatebutton']))
   {
      $id = $_POST['id'];

      $source_path = $_FILES['fileToUpload']['tmp_name'];
      $name = $_FILES['fileToUpload']['name'];
      $find_img = mysqli_query($conn, "SELECT pro_img FROM wp_product where id = '$id'");
      $product_img = mysqli_fetch_array($find_img);

      if( $name ==""){         
         $img = $product_img['pro_img'];
      }else{
         $rand = time().'_';
         $des_path =ABSPATH."wp-content/themes/mytheme/img/" . $rand.$name;
         move_uploaded_file($source_path,$des_path);
         $img = $rand.$name;
         unlink(ABSPATH."wp-content/themes/mytheme/img/" . $product_img['pro_img']);
      }
      $product_name        = trim($_POST['product_name']);
      $types_of_pro        = $_POST['types_of_pro'];
      $product_description = $_POST['product_description'];
      $recipe              = implode(',', $_POST['recipe']);
      $ingredients         = $_POST['ingredients'];
      $nutrition           = $_POST['nutrition'];

      global $wpdb;

      $proUpdate = $wpdb->query($wpdb->prepare(
          "UPDATE wp_product SET 
              product_name = '$product_name', 
              pro_cat = '$types_of_pro',
              product_description = '$product_description',
              recipe = '$recipe',
              ingredients = '$ingredients',
              nutrition = '$nutrition',
              pro_img = '$img'
              WHERE id = $id"
      ));        
       
      $wpdb->query('DELETE  FROM wp_product_recipe  WHERE product_id = "'.$id.'"');

         $recipe_table = "wp_product_recipe";
         foreach ($_POST['recipe'] as $key => $value) {
            $wpdb->insert( $recipe_table, array(
            'product_id'      => $id,
            'recipe_id'      => $value
            ));
         }
      if(count($proUpdate) > 0){
         $_SESSION['msg1'] = "Product updated!"; 
         wp_redirect( home_url('product-listing') );
      }
}
```


### Form Insert and inser data another table and image & name already exists
```php
   if(isset($_POST['SubmitButton']))
   {  
      global $wpdb;
      $product_table = "wp_product";

      $source_path = $_FILES['fileToUpload']['tmp_name'];
      $name = $_FILES['fileToUpload']['name'];
      $rand = time().'_';
      $des_path =ABSPATH."wp-content/themes/mytheme/img/" . $rand.$name;
      move_uploaded_file($source_path,$des_path);
      $img = $rand.$name;
      $barcode             = $_POST['barcode'];
      $product_name        = trim($_POST['product_name']);
      $types_of_pro        = $_POST['types_of_pro'];
      $product_description = $_POST['product_description'];
      $recipe              = implode(',', $_POST['recipe']); 

      $find_barcode = $wpdb->get_results( "SELECT barcode FROM $product_table where barcode = '$barcode'");
      $find_product = $wpdb->get_results( "SELECT product_name FROM $product_table where product_name = '$product_name'");

      if(count($find_barcode) > 0){
         $barcodemsg = 'Barcode Already exists!';
      }else if(count($find_product) > 0){
         $product_msg = 'Product Already exists!';
      }else{
         $sql = $wpdb->insert( $product_table, array(
         'user_id'      => $getuserid,
         'barcode'      => $barcode,
         'product_name' => $product_name,
         'pro_cat'      => $types_of_pro,
         'product_description' => $product_description,
         'recipe'       => $recipe,
         'pro_img'      => $img
      ));
         // Last Insert ID
         $lastid = $wpdb->insert_id;
         // Insert Data into Product_Recipe Table
         $recipe_table = "wp_product_recipe";
         $recipe1 = $_POST['recipe'];
         foreach ($recipe1 as $key => $value) {
            $wpdb->insert( $recipe_table, array(
            'product_id'      => $lastid,
            'recipe_id'      => $value
            ));
         }
	      if(count($sql) > 0){
		 $_SESSION['msg1'] = "New Product created successfully !"; 
		 wp_redirect( home_url('product-listing') );

	      }
      }
}
```

### Edit data in form
```php
if (isset($_GET['edit'])) {
  $id = $_GET['edit'];
  $record = $wpdb->get_results( "SELECT * FROM table_name where id=$id");
  foreach ($record as $key => $value) {
    $varibale              = $value->input_name;
    $varibale              = $value->input_name;
    $Recipe_exp           = explode(',',$value->recipe);
    $img_path             = home_url().'/wp-content/themes/mytheme/img/'.$value->pro_img;
  }
}
```
	
	
### Mail Function in php
```php
<?php
$toemail = "mksaxena27@gmail.com";
$subject = "Test Email";
$body = "Hi, This is test email send by PHP Script";

$headers = 'From: xyz@gmail.com'       . "\r\n" .
                 'Reply-To: zyz@gmail.com' . "\r\n" .
                 'X-Mailer: PHP/' . phpversion();
if (mail($toemail, $subject, $body, $headers)) {
echo "Email successfully sent to $toemail...";
} else {
echo "Email sending failed...";
} 
?>
```


### Some Link
https://bootsnipp.com/snippets/featured/image-gallery-with-fancybox (light box image gellery)<br>
https://www.ajax-zoom.com/examples/example5.php  (light box)<br>
http://www.elevateweb.co.uk/image-zoom/examples  (light box)<br>
https://de.rosler.com/fileadmin/ajax_zoom/examples/example6.php (light box)<br>
http://www.dwuser.com/education/content/click-to-zoom-for-photos-adding-lightbox-effect-to-your-images/ (light box)<br>
www.wp-hasty.com<br>
https://reduxframework.com/<br>


# Plugins
### contact form 7 recaptre:- 
https://wordpress.org/plugins/really-simple-captcha/#description shotcode:- [captchar captcha-1]

### Mathcaptcha:- 
https://wordpress.org/plugins/wp-math-captcha/

### Contact Form 7 – Conditional Fields
https://wordpress.org/plugins/cf7-conditional-fields/
```
[select* day1 "-- Select Your Day --" "Sunday" "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday"]

[group mon-wed]
[select* mon-wed "9:00 AM" "9:30 AM" "10:00 AM" "10:30 AM" "11:00 AM" "11:30 AM" "12:00 PM" "12:30 PM" "01:00 PM" "01:30 PM" "02:00 PM" "02:30 PM" "03:00 PM" "03:30 PM" "04:00 PM" "04:30 PM" "05:00 PM" "05:30 PM"]
[/group]

[group thr-sat]
[select* mon-wed "9:00 AM" "9:30 AM" "10:00 AM" "10:30 AM" "11:00 AM" "11:30 AM" "12:00 PM" "12:30 PM" "01:00 PM" "01:30 PM" "02:00 PM" "02:30 PM" "03:00 PM" "03:30 PM" "04:00 PM" "04:30 PM" "05:00 PM" "05:30 PM" "06:00 PM" "06:30 PM" "07:00 PM"]
[/group]

Conditinal field
show- mon-wed if day1 is equal to sunday 
show- thr-sat if day1 is equal to monday
```
### Advanced Custom Fields
https://wordpress.org/plugins/advanced-custom-fields/

### Popup Maker – Popup Forms
https://wordpress.org/plugins/popup-maker/ <br>
add class on button 

### All in one migration backup
https://wordpress.org/plugins/all-in-one-wp-migration/

### Wordpress Website speed increase plugin
https://wordpress.org/plugins/autoptimize/<br>
https://wordpress.org/plugins/w3-total-cache/

### Image compress Links
https://tinypng.com/<br>
https://imagecompressor.com/<br>
https://compressor.io/compress<br>
https://kraken.io/web-interface



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
extra code for cheking

1. logo lagane ke liye
	-> easy logo download karke install karke activate karke.
	->and appeaance mai easylogo mai jakr fill kar denge...
	->and uska sorte code uthakar html ki jaghe lga denage jha sa logo aa rha hai.
	<?php show_easylogo(); ?>
======================================================================================
2.	logo ka 2nd option
	<img src="images/logo.png"> ki jagha <?php twentysixteen_the_custom_logo(); ?>
========================================================================

slider ko dynamic banane ke liye......
================================================================================
===============
            --> <?php the_field("middele"); ?> //middle content ko call karane ke liye
            <?php the_field("service_work_process",8); ?>
==================
 <?php $args = array('post_type' => 'disease','posts_per_page'=>-1,'post_status' => 'publish'
  'category_name' => 'mobile-apps', 'order' => 'DESC' );

               $loop = new WP_Query( $args );

        while ( $loop->have_posts() ) : $loop->the_post();?>

        <div class="one_fourth btm last animate fadeInUp about-third-Section-size-1" data-anim-type="fadeInUp" data-anim-delay="800">

            <img src="<?php echo wp_get_attachment_url( get_post_thumbnail_id( $post->ID ));?>" class="about-third-Section-top_img" /> </img>

            <h4><?php echo $post->post_title ?></h4>

            <p><?php echo $post->post_content ?></p>  

        </div>         

<?php endwhile; ?>
----------------------------------------------
<a href="<?php echo get_permalink( $post->ID ); ?>"><?php echo substr($post->post_title, 0, 70);  ?>..</a><
====================================
<?php 
              $icon = array('icon-flag','icon-clock', 'icon-hotairballoon', 'icon-heart', 'icon-linegraph', 'icon-chat');
              $args = array('post_type' => 'chooseus','posts_per_page'=>-1,'post_status' => 'publish');

               $loop = new WP_Query( $args );
               $i='0';
        while ( $loop->have_posts() ) : $loop->the_post();?>
<div class="col-sm-6 col-md-4 col-lg-4">
            <div class="alt-features-item align-center">
                <div class="alt-features-icon">
                    <span class="<?php echo $icon[$i];?>"></span>
                </div>
                    <h3 class="alt-features-title font-alt"><?php echo $post->post_title ?></h3>
                <div class="alt-features-descr align-left">
                 <?php echo $post->post_content ?>
                </div>
            </div>
        </div>
        <?php $i++;endwhile; ?>

=================================================================================
wordpress ke deshboard mai admin menu badana
=================================================================================
<?php 
add_action( 'init', 'cptui_register_my_cpts_slider' );
function cptui_register_my_cpts_slider() {
	$labels = array(
		"name" => __( 'Slider', 'twentysixteen' ),
		"singular_name" => __( 'Slider', 'twentysixteen' ),
		);
	$args = array(
		"label" => __( 'Slider', 'twentysixteen' ),
		"labels" => $labels,
		'menu_icon'   => 'dashicons-format-gallery',
		"description" => "",
		"public" => true,
		"publicly_queryable" => true,
		"show_ui" => true,
		"show_in_rest" => false,
		"rest_base" => "",
		"has_archive" => false,
		"show_in_menu" => true,
		"exclude_from_search" => false,
		"capability_type" => "post",
		"map_meta_cap" => true,
		"hierarchical" => false,
		"rewrite" => array( "slug" => "slider", "with_front" => true ),
		"query_var" => true,
    //'taxonomies'  => array('category'),
		"supports" => array( "title", "editor", "thumbnail" ),);
	register_post_type( "slider", $args );
// End of cptui_register_my_cpts_banner()
}



contact form 7
          ============
          <div class="sendMessage formArea clearfix">
                  <ul class="row contactFormArea">
                    <li class="col-xs-12 col-sm-4 NoPaddingRight">[text* Name placeholder"Your Name"]</li>
                    <li class="col-xs-12 col-sm-4 NoPaddingRight">[email* Email placeholder"Your Email"]</li>
                    <li class="col-xs-12 col-sm-4">[tel* minlength:1 maxlength:10 Mobile placeholder"Phone Number"]</li>
                    <li class="col-xs-12 col-sm-12">[textarea* Textarea placeholder"Your Message..."]</li>
                    <div class="clearfix"></div>
                    <li class="col-sm-12 checkbox fromCheckBox text-center">
                     
                    </li>
                    <li class="col-sm-12">[submit class:submitBnt "Send mail"]</li>
                  </ul><!-- end of ul -->
                  <div id="simple-msg"></div>
                </div>
///<?php echo do_shortcode( '[contact-form-7 id="27" title="Contact form 1"]' ); ?>
particular page ke liye=============================
<?php if(is_page('projects')|| is_page('to-qualify')):?>
    <div class="col-sm-6">
  <?php endif; ?>


  remove_filter( 'the_content', 'wpautop' ); //remove the p and br
  =================================
  alternet loop
  =================================
  <?php $args = array('post_type' => 'profiles','posts_per_page'=>-1,'post_status' => 'publish');
              
               $loop = new WP_Query( $args );
               $i=0;
        while ( $loop->have_posts() ) : $loop->the_post();
         if($i%2==0){?>
            <div class="bordercol1">
               <div class="col-sm-2">
                 <div class="imgdiv">
                  <img src="<?php echo wp_get_attachment_url( get_post_thumbnail_id( $post->ID ));?>">
                 </div>
               </div>
               <div class="col-sm-10">
                  <div class="contenttext">
                     <h4><strong><?php echo $post->post_title ?></strong></h4>
                     <h5><strong>partner</strong></h5>
                     
                     <p><?php echo $post->post_content ?></p>
                  </div>
               </div>
            </div>
            <?php }else{?> 
              <div class="bordercol1">
                <div class="col-sm-10">
                <div class="contenttext">
                       <h4><strong><?php echo $post->post_title ?></strong></h4>
                       <h5><strong>partner</strong></h5>
                       
                       <p><?php echo $post->post_content ?></p>
                    </div>
                </div>
                <div class="col-sm-2">
                   <div class="imgdiv">
                    <img src="<?php echo wp_get_attachment_url( get_post_thumbnail_id( $post->ID ));?>">
                   </div>
                 </div>
              </div>
            <?php } $i++;?> 
            <?php endwhile; ?>
         </div>

=========================================================
//cutom field mai jab post banate hai
=========================================================
<section class="page-section">
   <div class="container relative">
      <div class="row">
         <div class="col-md-7 mb-sm-40">
            <!-- Gallery -->
            <div class="work-full-media mt-0 white-shadow wow fadeInUp">
               <ul class="clearlist work-full-slider owl-carousel">
                  <li>
                  <img src="<?php 
                           $appl1 = get_field("application_development" ,4); 
                            echo $appl1['url'];
                    
                    ?>" alt="" />
                    
                  </li>
                  <li>
                  <img src="<?php 
                           $appl1 = get_field("apIMG2" ,4); 
                            echo $appl1['url'];
                    
                    ?>" alt="" />
                    
                  </li>
               </ul>
            </div>
            <!-- End Gallery -->
         </div>
         <div class="col-md-5 col-lg-4 col-lg-offset-1">
            <!-- About Project -->
            <div class="text">
               
               <p>
                  <?php echo get_field("application_development_text" ,4); ?>  

                 </p>

            </div>
            <!-- End About Project -->
         </div>
      </div>
   </div>
</section>
==============================================================
