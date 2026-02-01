import axios from 'axios';

const API_BASE_URL = '/api';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const profileAPI = {
    getProfile: () => api.get('/profile'),
    getResearch: () => api.get('/research'),
    getEducation: () => api.get('/education'),
};

export const skillsAPI = {
    getSkills: () => api.get('/skills'),
    getSkillsGrouped: () => api.get('/skills/grouped'),
};

export const projectsAPI = {
    getProjects: (featured) => api.get('/projects', { params: { featured } }),
    getProject: (id) => api.get(`/projects/${id}`),
};

export const contactAPI = {
    sendMessage: (data) => api.post('/contact', data),
};

export const analyticsAPI = {
    trackPageView: (page, referrer) => api.post('/analytics/pageview', { page, referrer }),
    getStats: () => api.get('/analytics/stats'),
};

export default api;
