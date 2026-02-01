import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { profileAPI, skillsAPI } from '../services/api';
import ResumeCard from '../components/ResumeCard';
import SkillBadge from '../components/SkillBadge';
import { Download, User } from 'lucide-react';
import '../styles/about-me.css';

const AboutMe = () => {
    const [profile, setProfile] = useState(null);
    const [education, setEducation] = useState([]);
    const [skills, setSkills] = useState({});
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const [profileRes, eduRes, skillsRes] = await Promise.all([
                    profileAPI.getProfile(),
                    profileAPI.getEducation(),
                    skillsAPI.getSkillsGrouped(),
                ]);
                setProfile(profileRes.data);
                setEducation(eduRes.data);
                setSkills(skillsRes.data);
            } catch (error) {
                console.error('Error fetching about me data:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    if (loading) return <div className="loading">Loading...</div>;

    return (
        <div className="resume-page">
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="resume-header"
            >
                <div className="section-title-container">
                    <User className="section-icon" size={32} />
                    <h1 className="section-title">About Me</h1>
                </div>
                <a href="/resume.pdf" download className="btn btn-primary download-btn">
                    <Download size={20} /> Download CV
                </a>
            </motion.div>

            <section className="about-intro-section glass-card">
                <p className="about-bio">
                    {profile?.bio || 'AI/ML Engineer pursuing excellence in intelligent systems.'}
                </p>
                <div className="about-contact-brief">
                    <span>📍 {profile?.location || 'Hyderabad, India'}</span>
                    <span>✉️ {profile?.email || 'bhargavmadala2358@gmail.com'}</span>
                </div>
            </section>

            <section className="resume-section education-timeline">
                <h2 className="resume-section-title">Education</h2>
                <div className="timeline-container" style={{ marginTop: '20px' }}>
                    {education.map((item, index) => (
                        <ResumeCard
                            key={item.id}
                            title={item.degree}
                            subtitle={item.institution}
                            date={`${item.start_date} - ${item.end_date || 'Present'}`}
                            description={`GPA: ${item.gpa}`}
                            items={item.achievements}
                            isProminent={index === 0}
                        />
                    ))}
                </div>
                {education.length === 0 && <p className="no-data">No education records found.</p>}
            </section>

            <section className="resume-section">
                <h2 className="resume-section-title">Skills</h2>
                <div className="skills-container">
                    {Object.entries(skills).map(([category, items]) => (
                        <div key={category} className="skill-group glass-card">
                            <h3>{category}</h3>
                            <div className="skill-list">
                                {items.map((skill) => (
                                    <SkillBadge key={skill.id} name={skill.name} category={category} />
                                ))}
                            </div>
                        </div>
                    ))}
                    {Object.keys(skills).length === 0 && <p className="no-data">No skills found.</p>}
                </div>
            </section>
        </div>
    );
};

export default AboutMe;
