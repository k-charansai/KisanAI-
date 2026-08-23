// frontend/src/utils/animations.js
export const fadeInUp = {
  initial: { y: 20, opacity: 0 },
  animate: { y: 0, opacity: 1, transition: { duration: 0.6, ease: "easeOut" } },
  exit: { y: 20, opacity: 0, transition: { duration: 0.3 } }
};

export const leafGrow = {
  initial: { scale: 0, opacity: 0 },
  animate: { scale: 1, opacity: 1, transition: { duration: 1.2, ease: "elasticOut" } },
};

export const pulse = {
  initial: { scale: 1 },
  animate: { 
    scale: [1, 1.05, 1], 
    transition: { duration: 2, repeat: Infinity, ease: "easeInOut" } 
  },
};

export const leafUnfold = {
  initial: { rotate: -90, opacity: 0 },
  animate: { rotate: 0, opacity: 1, transition: { duration: 0.8, ease: "easeOut" } },
};

export const waterDropFill = {
  initial: { height: 0 },
  animate: { height: "100%", transition: { duration: 1.5, ease: "easeOut" } },
};

export const pollenFloat = {
  initial: { y: 0, opacity: 0 },
  animate: { 
    y: [-20, -40], 
    opacity: [0, 0.8, 0],
    transition: { duration: 3, repeat: Infinity, ease: "easeInOut" } 
  },
};