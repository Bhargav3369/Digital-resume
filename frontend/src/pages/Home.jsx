import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { profileAPI } from '../services/api';
import '../styles/home.css';

const Home = () => {
    const [profile, setProfile] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await profileAPI.getProfile();
                setProfile(response.data);
            } catch (error) {
                console.error('Error fetching profile:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchProfile();
    }, []);

    if (loading) return <div className="loading">Loading...</div>;

    return (
        <div className="home-page">
            <section className="hero">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8 }}
                    className="hero-content"
                >
                    <h1 className="hero-title">
                        Hi, I'm <span className="gradient-text">{profile?.full_name || 'Bhargav'}</span>
                    </h1>
                    <h2 className="hero-subtitle">{profile?.title || 'AI/ML Engineer'}</h2>
                    <p className="hero-bio">
                        {profile?.bio || 'Passionate about building intelligent systems and solving real-world problems with AI.'}
                    </p>
                    <div className="hero-actions">
                        <a href="/projects" className="btn btn-primary">View My Work</a>
                        <a href="/contact" className="btn btn-secondary">Get In Touch</a>
                    </div>
                </motion.div>

                <div className="hero-visual">
                    <div className="blob"></div>
                </div>
            </section>

            <section className="highlights">
                <div className="highlight-card glass-card">
                    <h3>Innovation</h3>
                    <p>Research-driven approach to AI/ML development.</p>
                </div>
                <div className="highlight-card glass-card">
                    <h3>Expertise</h3>
                    <p>Proficient in Computer Vision, NLP, and Reinforcement Learning.</p>
                </div>
                <div className="highlight-card glass-card">
                    <h3>Scalability</h3>
                    <p>Building modular and efficient software systems.</p>
                </div>
            </section>
        </div>
    );
};

export default Home;
