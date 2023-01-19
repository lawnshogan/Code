import React from 'react';
import './Gallery.css';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import { Carousel } from 'react-responsive-carousel';

export default function Gallery() {
  return (
    <div className="gallery" id="gallery">
      <Carousel
        autoPlay="true"
        infiniteLoop="true"
        showStatus="false"
        centerSlidePercentage={50}
      >
        <div>
          <img src="images/img1.jpg" alt="" />
        </div>
        <div>
          <img src="images/img2.jpg" alt="" />
        </div>
        <div>
          <img src="images/img3.jpg" alt="" />
        </div>
        <div>
          <img src="images/img4.jpg" alt="" />
        </div>
        <div>
          <img src="images/img5.jpg" alt="" />
        </div>
      </Carousel>
    </div>
  );
}
