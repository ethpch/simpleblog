function imgShow(outerdiv, innerdiv, bigimg, _this) {
    var src = _this.attr("src");//get src attribute of clicked _this element
    $(bigimg).attr("src", src);//set src of #bigimg

    /*get size of clicked image, and display popup window and big image */
    $("<img/>").attr("src", src).load(function () {
        var windowW = $(window).width();
        var windowH = $(window).height();
        var realWidth = this.width;
        var realHeight = this.height;
        var imgWidth, imgHeight;
        var scale = 0.8;//zoom size, zoom when size of image is bigger than window

        if (realHeight > windowH * scale) {
            imgHeight = windowH * scale;
            imgWidth = imgHeight / realHeight * realWidth;
            if (imgWidth > windowW * scale) {
                imgWidth = windowW * scale;
            }
        } else if (realWidth > windowW * scale) {
            imgWidth = windowW * scale;
            imgHeight = imgWidth / realWidth * realHeight;
        } else {
            imgWidth = realWidth;
            imgHeight = realHeight;
        }
        $(bigimg).css("width", imgWidth);//zoom as final width

        var w = (windowW - imgWidth) / 2;
        var h = (windowH - imgHeight) / 2;
        $(innerdiv).css({ "top": h, "left": w });
        $(outerdiv).fadeIn("fast");//fade-in #outerdiv and image
    });

    $(outerdiv).click(function () {//click again to fade-out
        $(this).fadeOut("fast");
    });
}