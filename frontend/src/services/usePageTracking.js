import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { analyticsAPI } from '../services/api';

const usePageTracking = () => {
    const location = useLocation();

    useEffect(() => {
        const trackPage = async () => {
            try {
                await analyticsAPI.trackPageView(
                    location.pathname + location.search,
                    document.referrer
                );
            } catch (error) {
                // Silently fail analytics so it doesn't break user experience
                console.debug('Analytics tracking failed:', error);
            }
        };
        trackPage();
    }, [location]);
};

export default usePageTracking;
