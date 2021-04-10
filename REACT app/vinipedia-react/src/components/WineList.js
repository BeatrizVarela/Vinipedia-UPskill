import Wine from './Wine';

export default function ( {wineData} ) {
    return (
        <>
            <h1 class="title">All Wines Listed</h1>
            <div class="list-container">
                { wineData.map((wine, id) => <Wine wine={wine} key={id} />)}
            </div>
            <hr/>
        </>
    )
}
