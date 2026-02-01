import React, { useState } from 'react';
import { FileText, ChevronDown, ChevronUp } from 'lucide-react';
import '../styles/project-card.css'; // Consistent card styles

const ResearchCard = ({ title, institution, date, description, status, skills, reportUrl }) => {
    const [isExpanded, setIsExpanded] = useState(false);
    const isLongDescription = description.length > 150;
    const displayDescription = isExpanded ? description : (isLongDescription ? `${description.substring(0, 150)}...` : description);

    return (
        <div className={`project-card glass-card ${isExpanded ? 'expanded' : ''}`}>
            <div className="project-info">
                <div className="project-header">
                    <h3 className="project-title">{title}</h3>
                    <span className="tech-tag" style={{ background: 'rgba(var(--accent-rgb), 0.1)', color: 'var(--accent-primary)' }}>
                        {status}
                    </span>
                </div>

                <h4 className="resume-card-subtitle" style={{ marginBottom: '10px', fontSize: '1rem' }}>{institution}</h4>
                <p className="resume-card-date" style={{ marginBottom: '15px', display: 'inline-block', width: 'fit-content' }}>{date}</p>

                <div className="project-description-container">
                    <p className="project-description">{displayDescription}</p>
                    {isLongDescription && (
                        <button
                            className="read-more-btn"
                            onClick={() => setIsExpanded(!isExpanded)}
                        >
                            {isExpanded ? (
                                <>Show Less <ChevronUp size={14} /></>
                            ) : (
                                <>Read More <ChevronDown size={14} /></>
                            )}
                        </button>
                    )}
                </div>

                {skills && (
                    <div className="project-tech">
                        {skills.split(',').map((skill, index) => (
                            <span key={index} className="tech-tag">{skill.trim()}</span>
                        ))}
                    </div>
                )}

                {reportUrl && (
                    <div className="project-links" style={{ borderTop: '1px solid rgba(255,255,255,0.05)', paddingTop: '15px' }}>
                        <a
                            href={reportUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="btn-report"
                            style={{ width: '100%', justifyContent: 'center' }}
                        >
                            <FileText size={18} /> Latest Report
                        </a>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ResearchCard;
