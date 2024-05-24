module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    screens: {
      sm: '576px',
      md: '768px',
      lg: '992px',
      xl: '1200px',
    },
    container: {
      center: true,
      padding: '1rem',
    },
    extend: {
      colors: {
        primary: '#FD3D57'
      },
      fontFamily:{
        poppins:  "'Poppins', sans-serif",
        roboto:  "'Roboto', sans-serif",
      },
    },
  },
  variants: {
    extend: {
      display: ['group-hover'],
      visibility: ['group-hover'],
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
// module.exports = {
//   content: [],
//   purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  // theme: {
  //   screens: {
  //     sm: '576px',
  //     md: '768px',
  //     lg: '992px',
  //     xl: '1200px',
  //   },
  //   container: {
  //     center: true,
  //     padding: '1rem',
  //   },
  //   extend: {
  //     colors: {
  //       primary: '#FD3D57'
  //     },
  //     fontFamily:{
  //       poppins:  "'Poppins', sans-serif",
  //       roboto:  "'Roboto', sans-serif",
  //     },
  //   },
  // },
  // variants: {
  //   extend: {
  //     display: ['group-hover'],
  //     visibility: ['group-hover'],
  //   },
  // },
//   plugins: [require('@tailwindcss/forms')],
// }

// module.exports = {
//   purge: [],
//   darkMode: false, // or 'media' or 'class'
//   theme: {
//     screens: {
//       sm: '576px',
//       md: '768px',
//       lg: '992px',
//       xl: '1200px',
//     },
//     container: {
//       center: true,
//       padding: '1rem',
//     },
//     extend: {
//       colors: {
//         primary: '#FD3D57'
//       },
//       fontFamily:{
//         poppins:  "'Poppins', sans-serif",
//         roboto:  "'Roboto', sans-serif",
//       }
//     },
//   },
//   variants: {
//     extend: {
//       visibility: ['group-hover'],
//       display: ['group-hover']
//     },
//   },
//   plugins: [require('@tailwindcss/forms')],
// }

