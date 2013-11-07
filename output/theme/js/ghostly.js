"use strict";

$(function(){
  var trigger = $("#nav-tags"),
    menu = $("#tag-menu"),
    tagMenuVisible = false;

  function showTagsMenu() {
    if (tagMenuVisible)
      return;

    tagMenuVisible = true;
    menu
      .css({
        display: "inline"
      })
      .transition({
        opacity: 1,
        top: "2.2em"
      }, 250);
  }

  function hideTagsMenu() {
    tagMenuVisible = false;
    menu.transition({
      opacity: 0,
      top: "2em"
    }, 250, function() {
      menu.css({
        display: "none"
      });
    });
  }

  trigger.on("mouseenter", showTagsMenu);
  $(".navbar").on("mouseleave", hideTagsMenu);

//  trigger.on("click", function(){
//    tagMenuVisible ? hideTagsMenu() : showTagsMenu();
//  });

});
