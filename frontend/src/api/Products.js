import API from './API'

class Products {
  static async all () {
    return API.get("/product")
  }

  static async sellers () {
    return API.get("/seller_product")
  }
}

export default Products

