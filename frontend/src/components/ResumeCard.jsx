import React from 'react';
import '../styles/resume-card.css';

const ResumeCard = ({ title, subtitle, date, description, items, isProminent }) => {
    // Extract GPA from description if it exists (assuming format "GPA: 7.5")
    const gpaMatch = description?.match(/GPA:\s*([\d.]+)/i);
    const gpa = gpaMatch ? gpaMatch[1] : null;

    return (
        <div className={`education-item ${isProminent ? 'prominent' : 'secondary'}`}>
            <div className="education-content">
                <div className="education-header">
                    <h3 className="education-degree">
                        {title}
                        {isProminent && <span className="current-badge">Current</span>}
                    </h3>
                    <div className="education-meta">
                        {date} {gpa && <span className="meta-separator">|</span>} {gpa && `GPA: ${gpa}`}
                    </div>
                </div>
                <h4 className="education-institution">{subtitle}</h4>

                {isProminent && items && (
                    <ul className="education-achievements">
                        {items.split(',').map((item, index) => (
                            <li key={index}>{item.trim()}</li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
};

export default ResumeCard;
