import Vue from 'vue'

class API {
  static async get (endpoint, options = {}) {
    endpoint = API._cleanEndpoint(endpoint)

    return Vue.axios.get(`${endpoint}`, options)
      .then((response) => {
        return Promise.resolve(response.data)
      })
  }

  static async post (endpoint, data = {}, options = {}) {
    endpoint = API._cleanEndpoint(endpoint)

    return Vue.axios.post(`${endpoint}`, data, options)
      .then((response) => {
        return Promise.resolve(response.data)
      })
  }

  static async patch (endpoint, data = {}, options = {}) {
    endpoint = API._cleanEndpoint(endpoint)

    return Vue.axios.patch(`${endpoint}`, data, options)
      .then((response) => {
        return Promise.resolve(response.data)
      })
  }

  static async put (endpoint, data = {}, options = {}) {
    endpoint = API._cleanEndpoint(endpoint)

    return Vue.axios.put(`${endpoint}`, data, options)
      .then((response) => {
        return Promise.resolve(response.data)
      })
  }

  static async delete (endpoint, data = {}, options = {}) {
    endpoint = API._cleanEndpoint(endpoint)

    return Vue.axios.delete(`${endpoint}`, data, options)
      .then((response) => {
        return Promise.resolve(response.data)
      })
  }

  static _cleanEndpoint (endpoint) {
    if (endpoint.startsWith('/')) {
      endpoint = endpoint.substring('/')
    }
    return endpoint
  }
}

export default API
