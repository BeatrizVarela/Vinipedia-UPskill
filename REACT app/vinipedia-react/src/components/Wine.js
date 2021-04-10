

export default function ( {wine} ) {
    return (
        <div className="list-element">
            <div className="wine-bottle-image">
                <img src={wine.picture}/>
            </div>
            <div className="wine-contents">
                <p>
                </p>
                <p>
                    <b>{ wine.name }</b>
                </p>
                <br/>
            </div>
        </div>
    )
}


