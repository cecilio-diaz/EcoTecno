import API from './API'

class Profile {
  static async all () {
    return API.get("/sellers")
  }

  static async get (id) {
    return API.get(`/sellers/${id}`)
  }
}

export default Profile

