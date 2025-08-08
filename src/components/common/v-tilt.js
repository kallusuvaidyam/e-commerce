export default {
  mounted(el) {
    el.addEventListener('mousemove', (e) => {
      const box = el.getBoundingClientRect()
      const x = e.clientX - box.left
      const y = e.clientY - box.top

      const centerX = box.width / 2
      const centerY = box.height / 2

      const rotateX = -(y - centerY) / 20
      const rotateY = (x - centerX) / 20

      el.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`
    })

    el.addEventListener('mouseleave', () => {
      el.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)'
    })
  }
}
