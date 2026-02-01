import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { profileAPI } from '../services/api';
import ResearchCard from '../components/ResearchCard';
import { Microscope } from 'lucide-react';
import '../styles/about-me.css';
import '../styles/projects.css'; // For grid layout

const Research = () => {
    const [research, setResearch] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await profileAPI.getResearch();
                setResearch(response.data);
            } catch (error) {
                console.error('Error fetching research data:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    if (loading) return <div className="loading">Loading...</div>;

    // Hardcoded skills for the research project as requested by user
    const researchSkills = "Reinforcement Learning, Actor–Critic Methods (CACLA), Human-in-the-loop Learning, Reward Shaping, Continuous Control, Python";

    return (
        <div className="research-page" style={{ paddingBottom: 'var(--spacing-lg)' }}>
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="resume-header"
            >
                <div className="section-title-container">
                    <Microscope className="section-icon" size={32} />
                    <h1 className="section-title">Research Work</h1>
                </div>
            </motion.div>

            <div className="projects-grid">
                {research.map((item, index) => (
                    <motion.div
                        key={item.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.1 }}
                    >
                        <ResearchCard
                            title={item.title}
                            institution={item.institution}
                            date={`${item.start_date} - ${item.end_date || 'Present'}`}
                            description={item.description}
                            status={item.status}
                            skills={researchSkills}
                            reportUrl={item.publication_url}
                        />
                    </motion.div>
                ))}
            </div>

            {research.length === 0 && (
                <p className="no-data">No research projects found at the moment.</p>
            )}
        </div>
    );
};

export default Research;
