export const accessToken = `5bd804d850e5f0ea24517a3a40da0839425551ab`;

export const wineListDataURL = (start, qty) =>
  `https://winecense.herokuapp.com/api/wines/?limit=${qty || 16}&offset=${
    start || 0
  }`;

export const detailsUrlForWineWithId = (id) =>
  `https://winecense.herokuapp.com/api/wines/${id}`;
