
export const wineListDataURL = (start, qty) => `https://winecense.herokuapp.com/api/wines/?limit=${qty || 16}&offset=${start || 0}`;

export const detailsUrlForWineWithId = id => `https://winecense.herokuapp.com/api/wines/${id}`;