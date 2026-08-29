function SectionHeader({ eyebrow, title, action }) {
  return (
    <div className="section-header">
      <div>
        {eyebrow && (
          <p className="section-eyebrow">
            {eyebrow}
          </p>
        )}

        <h2>{title}</h2>
      </div>

      {action && (
        <button className="section-action">
          {action}
        </button>
      )}
    </div>
  );
}

export default SectionHeader;
