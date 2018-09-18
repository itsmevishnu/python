<?php

/*** Child Theme Function  ***/

function vibez_elated_child_theme_enqueue_scripts() {
	
	$parent_style = 'vibez_elated_default_style';
	
	wp_enqueue_style('vibez_elated_child_style', get_stylesheet_directory_uri() . '/style.css', array($parent_style));
}

add_action( 'wp_enqueue_scripts', 'vibez_elated_child_theme_enqueue_scripts' );


/** add new classess to the blog **/
function vibez_special_nav_class( $classes, $item ) {
	if( ( is_single() || is_author() || is_category() || is_date() ) && $item->title == 'Blog' ) {
    // if( is_single() && $item->title == 'Blog'  || is_category() && $item->title == 'Blog' || is_author() && $item->title == 'Blog' ){
        $classes[] = 'current-menu-item page_item current_page_item eltdf-active-item';
    }
    return $classes;
}
add_filter( 'nav_menu_css_class', 'vibez_special_nav_class', 10, 2 );