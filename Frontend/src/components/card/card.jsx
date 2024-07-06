import React from 'react'
import "./card.css"

function card() {
  return (
    <div className='cart__container'>
    <div className="card">
      {/* <span
        className={`${count !== 0 ? "card__badge" : "card__badge--hidden"}`}
      >
        {count}
      </span> */}
      <div className="image__container">
        {/* <img src={Image} alt={title} /> */}
      </div>
      <h4 className="card__title">
        {/* {title} . <span className="card__price">$ {price}</span> */}
      </h4>

      <div className="btn-container">
        {/* <Button title={"+"} type={"add"} onClick={handleIncrement} />
        {count !== 0 ? (
          <Button title={"-"} type={"remove"} onClick={handleDecrement} />
        ) : (
          ""
        )} */}
      </div>
    </div>
    </div>
  )
}

export default card
