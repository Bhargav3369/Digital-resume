import React from 'react';
import '../styles/skill-badge.css';

const SkillBadge = ({ name, category }) => {
    return (
        <div className={`skill-badge ${category.toLowerCase().replace(/\s+/g, '-')}`}>
            {name}
        </div>
    );
};

export default SkillBadge;
