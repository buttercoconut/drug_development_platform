import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 10000,
})

export default {
  getDrugCandidates() {
    return apiClient.get('/drug-candidates')
  },
  getClinicalData() {
    return apiClient.get('/clinical-data')
  },
}
