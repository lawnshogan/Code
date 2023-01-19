import React from 'react';

import './ourStory.css';

export default function OurStory() {
  return (
    <div className="ourStory" id="story">
      <div className="title">
        <span>OUR STORY</span>
        <h1>With love</h1>
      </div>
      {/* <img src="images/nobackground.png" alt="" /> */}

      <div className="story">
        <div className="vl" />
        <div className="content content1">
          <span className="date">2009</span>
          <h1>How we met </h1>
          <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit.</p>
          <p>
            Lorem, ipsum dolor sit amet consectetur adipisicing elit consectetur
            adipisicing elit. .
          </p>
        </div>

        <div className="photo1">
          <img src="images/croppedImage1.png" alt="" />
        </div>

        <div className=" content content2">
          <span className="date">2019</span>
          <h1>Proposal </h1>
          <p>
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum
            quisquam cumque officiis illum. repellendus et nulla, distinctio
            corporis placeat neque aperiam at id eveniet amet doloremque nihil.
          </p>
        </div>
        <div className="photo2">
          <img src="images/cropped-image2.jpg" alt="" />
        </div>

        <div className=" content content3">
          <span className="date">2020</span>
          <h1>Our Wedding </h1>
          <p>
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum
            quisquam cumque officiis illum
          </p>
        </div>
        <div className="photo3">
          <img src="images/cropped-image3.jpg" alt="" />
        </div>
      </div>
    </div>
  );
}
