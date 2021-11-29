import Axios from 'axios';

export default {
    async retrieveCountryList(page_size, page) {
      return new Promise((resolve) => {
        Axios.get(
          'http://127.0.0.1:8000/api/v1/analysis/countries/',
          {}
        ).then((response) => {
          resolve(response.data);
        });
      });
    },
}
